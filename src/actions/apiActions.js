import * as types from './actionTypes';

export function listEntries(entries) {
  return {
    type: types.API_FETCH_ROOT,
    entries,
  };
}

export function getEntry(slug, entry) {
  return {
    type: types.API_FETCH_SLUG,
    slug,
    entry,
  };
}

export function hideOverlay() {
  return {
    type: types.API_HIDE_OVERLAY,
  };
}
