import "./App.css";
import Form from "./components/Form";
import Header from "./components/Header";
import Models from "./components/Models";

function App() {
  return (
    <main>
      <div className="main">
        <div className="gradient" />
      </div>
      <div className="app">
        <Header />
        <Form />
        <Models />
      </div>
    </main>
  );
}

export default App;
