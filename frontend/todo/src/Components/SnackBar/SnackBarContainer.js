import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { setSnackBarState } from "../../actions/snackBarAction.js";
import SnackbarComponent from "./SnackBarComponent.js";

function SnackbarContainer() {
    const dispatch = useDispatch();
    const {
        snackBarOpen,
        snackBarContent,
        snackBarVariant,
        autoHideDuration,
    } = useSelector((state) => state.snackBarReducer);

    function onCloseSnackBar() {
        dispatch(
            setSnackBarState({
                snackBarOpen: false,
            })
        );
    }

    return (
        <SnackbarComponent
            onCloseSnackBar={onCloseSnackBar}
            snackBarOpen={snackBarOpen}
            snackBarVariant={snackBarVariant}
            snackBarContent={snackBarContent}
            autoHideDuration={autoHideDuration}
        />
    );
}

export default SnackbarContainer;
