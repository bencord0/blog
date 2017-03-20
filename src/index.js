import React from 'react';
import {Provider} from 'react-redux';
import {createStore} from 'redux';

import Index from './containers/Index';
import handleActions from './reducers';

const store = createStore(handleActions)

const Fragments = () => {
  return (
    <Provider store={store}>
      <Index />
    </Provider>
  );
}

export default Fragments
