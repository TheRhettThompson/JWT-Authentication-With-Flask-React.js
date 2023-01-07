const getState = ({ getStore, getActions, setStore }) => {
	return {

		//update store to reflect what we want to use from the backend
		store: {
			api: "https://3001-therhetttho-jwtauthenti-agjeiu81f96.ws-us81.gitpod.io/"
			isAuthenticated: false
		},

		//Add sign-up fetch request as an Action
		actions: {
			// Use getActions to call a function within a fuction
			//exampleFunction: () => {
				//getActions().changeColor(0, "green");
			sign_up: (email, password) => {
				const store = getStore();

				fetch(`${store.api}/api/signup` {
					method: "POST",
					body: JSON.stringify({
						email: email,
						password: password
					}),
					Headers: {
						"Content-type": "application/json"
					}
				})
					.then(resp => {
						if (resp.ok) {
							return resp.json();
						}
					})
					.then(data => {
						localStorage.setItem("token", data.token);
						setStore({ isAuthenticated: true});
					})

					.catch(error => console.log("Error during login", error))

			}
			},
		
			loadData: () =>{
				const store = getStore();

				fetch(`${}`)
			}


			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
