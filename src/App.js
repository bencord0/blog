import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';

import Navigation from './Navigation';
import Home from './Home';
import Entry from './Entry';
import About from './About';
import Archive from './Archive';
import RecentPosts from './RecentPosts';
import Feeds from './Feeds';

import { Col, Grid, Row } from 'react-bootstrap';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

class App_ extends Component {
  render() {
    return (
      <React.Fragment>
        <Navigation/>
        <Grid>
          <Row>
            <Col xs={8}>
              <Switch>
                <Route exact path="/" component={Home}/>
                <Route path="/about/" component={About}/>
                <Route path="/archive/" component={Archive}/>
                <Route path="/:slug/" component={Entry}/>
              </Switch>
            </Col>
            <Col xs={4}>
              <RecentPosts/>
              <Feeds/>
            </Col>
          </Row>
        </Grid>
     </React.Fragment>
    );
  }
}

const App = () => (
  <BrowserRouter>
    <App_/>
  </BrowserRouter>
);
export default App;
