import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';

function EntryItem(props) {
  const {
    date, title, slug, summary,
  } = props;
  return (
    <li>
      <h2>{ title }</h2>
      <h6><Link to={`/${slug}/`}>{ date }</Link></h6>
      { summary }
    </li>
  );
}

EntryItem.propTypes = {
  date: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  slug: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
};

export default EntryItem;
