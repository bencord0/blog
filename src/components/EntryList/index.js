import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import EntryItem from 'components/EntryItem';

import './index.css';

function EntryList(props) {
  const { entries } = props;
  return (
    <div className="EntryList">
      <ul>
        {
          Object.keys(entries).map(
            slug => <EntryItem key={slug} {...entries[slug]} />,
          )
        }
      </ul>
    </div>
  );
}

EntryList.propTypes = {
  entries: PropTypes.object.isRequired,
};

function mapStateToProps(state) {
  const { entries } = state;
  return {
    entries,
  };
}

export default connect(mapStateToProps)(EntryList);
