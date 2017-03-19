import React, {Component} from 'react';
import {View} from 'react-native';

import styles from '../../styles';


export default class Overlay extends Component {
  render() {
    if (this.props.showOverlay) {
      return (
        <View style={styles.overlay}>
          {this.props.children}
        </View>
      );
    } else {
      return <View />;
    }
  }
}
