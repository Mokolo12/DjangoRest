import Menu from "./components/Menu";
import Footer from "./components/Footer";

const apiUrl = 'http://localhost:8000/api/';
const getUrl = (name) => `${apiUrl}${name}`;

class App extends React.Component {
    constructor(props) {
	@@ -17,7 +17,7 @@ class App extends React.Component {
    }

    componentDidMount() {
        axios.get(getUrl('users'))
            .then(response => {
                const users = response.data;
                this.setState(