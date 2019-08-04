import React from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';

function RecentEntries(props) {
  const { entries } = props;

  return (
    <React.Fragment>
      <h3>Recent Posts</h3>
      <ul>
        {
          Object.keys(entries).map(slug => {
            const { title } = entries[slug];
            return (
              <li key={slug}>
                <Link to={`/${slug}/`}>
                  {title}
                </Link>
              </li>
            );
          })
        }
      </ul>
    </React.Fragment>
  );
}

RecentEntries.propTypes = {
  entries: PropTypes.object.isRequired,
};

function mapStateToProps(state) {
  const { entries } = state;
  return {
    entries,
  };
}

export default connect(mapStateToProps)(RecentEntries);
