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
      };
    case types.API_FETCH_SLUG:
      return {
        ...state,
      };
    default:
      return state;
  }
}
