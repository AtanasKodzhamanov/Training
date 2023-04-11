export function getUserData() {
    return JSON.parse(sessionStorage.getItem("user"));
}

export function getAccessToken() {
    const user = getUserData();
    if (user) {
        return user.accessToken;
    } else {
        return null;
    }
}

export function setUserData() {
    sessionStorage.setItem("user", JSON.stringify(data));
}

export function clearUserData() {
    sessionStorage.removeItem("user")
}