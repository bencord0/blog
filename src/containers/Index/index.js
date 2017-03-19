import React, { Component } from 'react';
import {
  Button,
  Text,
  ScrollView,
  View
} from 'react-native';

import Overlay from '../../components/Overlay';
import styles from '../../styles';

export default class Index extends Component {

  constructor(props) {
    super(props);
    this.state = {
      showOverlay: false,
      entries: [],
      currentEntry: {content: ""},
    };

    this.showOverlay = this.showOverlay.bind(this);
  }

  componentDidMount() {
    this.fetchPost();
  }

  async fetchPost() {
    try {
      let response = await fetch('https://blog.condi.me/api/');
      let entries = await response.json();

      this.setState({
        entries: entries
      });

    } catch(error) {
      console.log(error);
    }

  }

  async showOverlay(slug) {
    try {
      let req = await fetch(`https://blog.condi.me/api/${slug}/`);
      let entry = await req.json();

      this.setState({
        showOverlay: true,
        currentEntry: entry
      });
    } catch(error) {
      console.log(error);
    }
  }

  render() {
    let entries = this.state.entries.map(entry => {
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
        <Overlay showOverlay={this.state.showOverlay}>
          <ScrollView >
            <Text
              style={styles.entry}
              onPress={() => this.setState({showOverlay: false})}
            >
              {this.state.currentEntry.content}
            </Text>
          </ScrollView>
        </Overlay>
      </View>
    );
  }
}
