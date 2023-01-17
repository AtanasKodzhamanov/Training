const baseURL = "http://localhost:3030/users";


const save = (user) => {
    if (user) {
        localStorage.setItem("accessToken", user.accessToken);
        localStorage.setItem("email", user.email);
        localStorage.setItem("id", user._id);
        localStorage.setItem("username", user.username);
    }
};

export const login = (email, password) => {
    return fetch(`${baseURL}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email, password})
    })
        .then(res => res.json())
        .then(user=> {
            save(user)

            return user;
    });
}

export const isAuthenticated = () => {
    let accessToken = localStorage.getItem("accessToken");
    return Boolean(accessToken);
}