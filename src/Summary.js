import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Summary extends Component {
  constructor(props) {
    super(props);
    console.log("Summary: constructor");

    this.state = {
      entry: {}
    }
  }

  componentDidMount() {
    console.log("Summary: componentDidMount");
    const { slug } = this.props.entry;
    this.fetchContent(slug);
  }

  fetchContent(slug) {
    if (slug && !this.state.summary) {
      console.log(`Summary: fetching ${slug}`);
      fetch(`https://blog.condi.me/api/${slug}/`)
        .then(res => res.json())
        .then(res => setTimeout(() =>    this.setState({entry: res})    , 5000))
    }
  }

  render() {
    const { slug, title, date } = this.props.entry;
    let html_url = `/${slug}/`;
    let fuzzy_date = date;
    let summary = "";
    if ("summary" in this.state.entry) {
       html_url = this.state.entry.html_url;
       fuzzy_date = this.state.entry.fuzzy_date;
       summary = this.state.entry.summary;
    }
    console.log(`Summary: render ${title}`);

    return (
      <div>
        <h2><Link to={html_url}>{title}</Link></h2>
        <h6>posted {fuzzy_date} by <Link to="/about/">Ben Cordero</Link>.</h6>
        <div dangerouslySetInnerHTML={ {__html: summary} }/>
        <div>
          <p><Link to={html_url}>Read more</Link></p>
        </div>
      </div>
    );
  }
}

export default Summary;
