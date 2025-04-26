import {
    OPEN_LOGIN_DIALOG,
    CLOSE_LOGIN_DIALOG,
} from "../actions/loginDialogAction.js";
import { initialDialogState } from "./initialState.js";

export function loginDialogReducer(state = initialDialogState, action) {
    switch (action.type) {
        case OPEN_LOGIN_DIALOG:
            return {
                ...state,
                dialogOpen: true,
            };

        case CLOSE_LOGIN_DIALOG:
            return {
                ...state,
                dialogOpen: false,
            };
        default:
            return {
                ...state,
            };
    }
}
