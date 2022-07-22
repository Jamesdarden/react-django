import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools } from "redux-devtools-extension"; //set up for chrome extension
import thunk from "redux-thunk"; //middleware
import rootReducer from "./reducers"; //looks for a folder reducer for index.js  // meeting place for all reducers

const initialState = {};

const middleware = [thunk];

const store = createStore(
  rootReducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
