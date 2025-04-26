import { combineReducers } from "redux";
import { authReducer } from "./authReducer.js";
import { todoReducer } from "./todoReducer.js";
import { todoDisplayFilterReducer } from "./todoDisplayFilterReducer.js";
import { snackBarReducer } from "./snackBarReducer.js";
import { loginDialogReducer } from "./loginDialogReducer.js";
import { signUpDialogReducer } from "./signUpDialogReducer.js";

const reducer = combineReducers({
    authReducer,
    todoReducer,
    todoDisplayFilterReducer,
    snackBarReducer,
    loginDialogReducer,
    signUpDialogReducer,
});

export default reducer;
