import React, { useEffect } from "react";
import UserInfoComponent from "./UserInfoComponent.js";
import { useDispatch, useSelector } from "react-redux";
import { openLoginDialog } from "../../actions/loginDialogAction.js";
import { openSignUpDialog } from "../../actions/signUpDialogAction.js";
import { loginUser, fetchLogoutUser } from "../../actions/authAction.js";
import Cookies from "universal-cookie";

const cookies = new Cookies();

function UserInfoContainer() {
    const dispatch = useDispatch();
    const { user, isLoggedIn } = useSelector((state) => state.authReducer);

    function onClickLoginButton() {
        dispatch(openLoginDialog());
    }

    function onClickSignUpButton() {
        dispatch(openSignUpDialog());
    }

    function onClickLogoutButton() {
        dispatch(fetchLogoutUser());
    }

    const cookieUser = cookies.get("User");

    useEffect(() => {
        if (cookieUser) {
            dispatch(loginUser(cookieUser));
        }
    }, [dispatch, cookieUser]);

    return (
        <UserInfoComponent
            isLoggedIn={isLoggedIn}
            user={user}
            onClickLoginButton={onClickLoginButton}
            onClickLogoutButton={onClickLogoutButton}
            onClickSignUpButton={onClickSignUpButton}
        />
    );
}

export default UserInfoContainer;
