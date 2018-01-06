import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Archive extends Component {
  constructor(props) {
    super(props);
    console.log("Archive: constructor");

    this.state = {
      content: []
    }
  }

  componentDidMount() {
    console.log("Archive: componentDidMount");
    this.fetchContent();
  }

  fetchContent() {
    console.log("Archive: fetching content");
    fetch("https://blog.condi.me/api/")
      .then(res => res.json())
      .then(res => this.setState({
        content: res
      }))
  }

  render() {
    return (
      <React.Fragment>
      {this.state.content.map(
        (entry, index) => {
          return (
            <h6 key={index}><Link to={`/${entry.slug}/`}>{entry.title}</Link></h6>
          );
        }
      )}
      </React.Fragment>
    );
  }
}

export default Archive;
