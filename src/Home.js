import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import Summary from './Summary';

class Home_ extends Component {
  constructor(props) {
    super(props);
    console.log("Home: constructor");

    this.state = {
      content: []
    };
  }

  componentDidMount() {
    console.log("Home: componentDidMount");
    this.fetchContent();
  }

  componentWillReceiveProps(nextProps) {
    console.log("Home: componentWillReceiveProps");
    this.fetchContent();
  }

  fetchContent() {
    console.log("Home: fetching content");
    fetch("https://blog.condi.me/api/")
      .then(res => res.json())
      .then(res => this.setState({
        content: res.slice(0, 20)
      }))
  }

  componentWillUnmount() {
    console.log("Home: componentWillUnmount")
  }

  shouldcomponentUpdate(nextProps, nextState) {
    return true;
  }

  render() {
    console.log("Home render");

    return (
      <React.Fragment>
        {this.state.content && this.state.content.map(
          (entry, index) => {
            return <Summary key={index} entry={entry}/>;
          }
        )}
      </React.Fragment>
    );
  }
}

const Home = withRouter(Home_);
export default Home;
