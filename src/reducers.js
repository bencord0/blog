import * as types from './actions/actionTypes';

const initialState = {
  showOverlay: false,
  entries: [],
  currentEntry: {content: ""},
};

export default (state = initialState, action = {}) => {
  switch (action.type) {
    case types.API_FETCH_ROOT:
      return {
        ...state,
        entries: action.entries,
      };
    case types.API_FETCH_SLUG:
      return {
        ...state,
        currentEntry: action.entry,
        showOverlay: true,
      };
    case types.API_HIDE_OVERLAY:
      return {
        ...state,
        showOverlay: false,
      };
    default:
      return state;
  }
}
