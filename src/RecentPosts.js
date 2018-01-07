import React, { Component } from "react";
import { Link } from "react-router-dom";

class RecentPosts extends Component {
  constructor(props) {
    super(props);
    console.log("RecentPosts: constructor");

    this.state = {
      content: []
    };
  }

  componentDidMount() {
    console.log("RecentPosts: componentDidMount");
    this.fetchContent();
  }

  fetchContent() {
    console.log("RecentPosts: fetching content");
    fetch("https://blog.condi.me/api/")
      .then(res => res.json())
      .then(res => this.setState({
        content: res.slice(0, 20)
      }));
  }

  render() {
    return (
      <React.Fragment>
        <h3>Recent Posts</h3>
        <ul className="list-unstyled">
          {this.state.content.map(
            (entry, index) => {
              return (
                <li key={index}><Link to={`/${entry.slug}/`}>{entry.title}</Link></li>
              );
            })
          }
        </ul>
      </React.Fragment>
    );
  }
}

export default RecentPosts;
