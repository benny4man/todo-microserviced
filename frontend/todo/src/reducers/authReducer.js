import { LOGIN_USER, LOGOUT_USER } from "../actions/authAction.js";
import { initialLoggedInState } from "./initialState.js";
import Cookies from "universal-cookie";

const cookies = new Cookies();

export function authReducer(state = initialLoggedInState, action) {
    switch (action.type) {
        case LOGIN_USER:
            return {
                ...state,
                isLoggedIn: true,
                user: action.user,
            };

        case LOGOUT_USER:
            cookies.remove("Access-Token");
            cookies.remove("User");

            return {
                ...initialLoggedInState,
            };

        default:
            return state;
    }
}
