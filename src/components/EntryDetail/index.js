import React from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';

function EntryDetail(props) {
  const { title, summary } = props;
  return (
    <React.Fragment>
      <h1>{title}</h1>
      <p>{summary}</p>
    </React.Fragment>
  );
}

EntryDetail.propTypes = {
  title: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
};

function mapStateToProps(state, ownProps) {
  const { slug } = ownProps.match.params;
  const entry = state.entries[slug] || { title: '', summary: '' };
  const { summary, title } = entry;

  return {
    slug,
    title,
    summary,
  };
}

export default withRouter(connect(mapStateToProps)(EntryDetail));
