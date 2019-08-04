import React from 'react';
import { connect } from 'react-redux';
import { Route } from 'react-router-dom';
import PropTypes from 'prop-types';
import { items } from 'static-data';

import About from 'components/About';
import Archive from 'components/Archive';
import EntryDetail from 'components/EntryDetail';
import EntryList from 'components/EntryList';
import Nav from 'components/Nav';
import RecentEntries from 'components/RecentEntries';

import { addEntrySummary } from 'actions';

import './index.css';

class App extends React.Component {
  static propTypes = {
    dispatch: PropTypes.func.isRequired,
  }

  componentDidMount() {
    const { dispatch } = this.props;
    items.map(item => dispatch(addEntrySummary(
      item.slug,
      item.title,
      item.date,
      item.summary,
    )));
  }

  render() {
    return (
      <div className="App">
        <nav className="App-nav">
          <Nav />
        </nav>
        <div className="App-main">
          <div className="App-content">
            <Route path="/" exact component={EntryList} />
            <Route path="/about/" exact component={About} />
            <Route path="/archive/" exact component={Archive} />
            <Route path="/:slug/" component={EntryDetail} />
          </div>
          <div className="App-sidebar">
            <RecentEntries />
          </div>
        </div>
      </div>
    );
  }
}

export default connect()(App);
