import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import ProjectList from './components/Project';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

const apiUrl = 'http://localhost:8000/api/';
const getUrl = (name) => `${apiUrl}${name}`;
	@@ -12,7 +14,8 @@ class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': []
        };
    }

	@@ -27,15 +30,38 @@ class App extends React.Component {
                );
            })
            .catch(error => console.error(error));
        axios.get(getUrl('projects'))
            .then(response => {
                const projects = response.data;
                this.setState(
                    {
                        projects
                    }
                );
            })
            .catch(error => console.error(error));
    }

    render() {
        return (
            <Router>
                <Menu/>
                <Switch>
                    <Route
                        path='/users'
                        render={(props) => (
                            <UserList {...props} users={this.state.users}/>
                        )}
                    />
                    <Route
                        path='/projects'
                        render={(props) => (
                            <ProjectList {...props} projects={this.state.projects}/>
                        )}
                    />
                </Switch>
                <Footer/>
            </Router>
        );
    }
}