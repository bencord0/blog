import React, { Component } from "react";
import { Link, withRouter } from "react-router-dom";

class Entry_ extends Component {
  constructor(props) {
    super(props);
    console.log("Entry: constructor");

    this.state = {};
  }

  componentDidMount() {
    console.log("Entry: componentDidMount");
    const { slug } = this.props.match.params;
    this.fetchContent(slug);
  }

  componentWillReceiveProps(nextProps) {
    console.log("Entry: componentWillReceiveProps");
    const { slug } = nextProps.match.params;
    this.fetchContent(slug);
  }

  fetchContent(slug) {
    if (slug && !(slug in this.state)) {
      console.log(`Entry: fetching ${slug}`);
      fetch(`https://blog.condi.me/api/${slug}/`)
        .then(res => res.json())
        .then(res => {
          let update = {};
          update[slug] = res;
          this.setState(update);
        });
    }
  }

  componentWillUnmount() {
    console.log("Entry: componentWillUnmount");
  }

  renderHtmlForSlug(slug) {
    const entry = this.state[slug];

    if (entry) {
      return {
        __html: entry.html
      };
    }
    return {__html: ""};
  }

  render() {

    const { slug } = this.props.match.params;
    const entry = this.state[slug];
    console.log(`Entry: render ${slug}`);

    if (entry) {
      return (
        <React.Fragment>
          <h2><Link to={entry.html_url}>{entry.title}</Link></h2>
          <h6>posted {entry.fuzzy_date} by <Link to="/about/">Ben Cordero</Link></h6>
          <div dangerouslySetInnerHTML={ this.renderHtmlForSlug(slug) }/>
        </React.Fragment>
      );

    }

    return (
      <React.Fragment>
        <h2>Loading ...</h2>
        <h6>fetching post...</h6>
        <div/>
      </React.Fragment>
    );
  }
}

const Entry = withRouter(Entry_);
export default Entry;
