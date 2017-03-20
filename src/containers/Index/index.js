import React, { Component } from 'react';
import {
  Button,
  Text,
  ScrollView,
  View
} from 'react-native';
import {connect} from 'react-redux';

import Overlay from '../../components/Overlay';
import styles from '../../styles';

import {listEntries, getEntry, hideOverlay} from '../../actions/apiActions';

class Index extends Component {

  constructor(props) {
    super(props);

    this.showOverlay = this.showOverlay.bind(this);
    this.fetchPosts = this.fetchPosts.bind(this);
  }

  componentDidMount() {
    this.fetchPosts();
  }

  async fetchPosts() {
    try {
      let response = await fetch('https://blog.condi.me/api/');
      let entries = await response.json();

      this.props.onListEntries(entries);

    } catch(error) {
      console.log(error);
    }

  }

  async showOverlay(slug) {
    try {
      let req = await fetch(`https://blog.condi.me/api/${slug}/`);
      let entry = await req.json();

      this.props.onGetEntry(entry.slug, entry)
    } catch(error) {
      console.log(error);
    }
  }

  render() {

    let entries = this.props.entries.map(entry => {
      return (
        <Button
          key={entry.slug}
          onPress={() => this.showOverlay(entry.slug)}
          title={entry.title}
        />
      );
    });

    return (
      <View style={styles.container}>
        <ScrollView >
          {entries}
        </ScrollView>
        <Overlay showOverlay={this.props.showOverlay}>
          <ScrollView >
            <Text
              style={styles.entry}
              onPress={this.props.onHideOverlay}
            >
              {this.props.currentEntry.content}
            </Text>
          </ScrollView>
        </Overlay>
      </View>
    );
  }
}

function mapStateToProps(state, ownProps) {
  return {
    entries: state.entries,
    showOverlay: state.showOverlay,
    currentEntry: state.currentEntry,
  };
}

function mapDispatchToProps(dispatch) {
  return {
    onListEntries: (entries) => {
      dispatch(listEntries(entries));
    },
    onGetEntry: (slug, entry) => {
      dispatch(getEntry(slug, entry));
    },
    onHideOverlay: () => {
      dispatch(hideOverlay());
    },
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Index);
