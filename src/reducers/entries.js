const initialState = {};

function entries(state = initialState, action) {
  switch (action.type) {
    case 'ADD_ENTRY_SUMMARY': {
      const {
        slug,
        title,
        date,
        summary,
      } = action;

      return {
        ...state,
        [action.slug]: {
          slug,
          title,
          date,
          summary,
        },
      };
    }
    default:
      return state;
  }
}

export default entries;
