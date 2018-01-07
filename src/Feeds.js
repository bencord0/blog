import React, { Component } from "react";

class About extends Component {
  render() {
    return (
      <React.Fragment>
        <h3>Feeds</h3>
        <a href="https://blog.condi.me/feeds/atom/">Atom</a>
          &nbsp;/&nbsp;
        <a href="https://blog.condi.me/feeds/rss/">RSS</a>
      </React.Fragment>
    );
  }
}

export default About;
