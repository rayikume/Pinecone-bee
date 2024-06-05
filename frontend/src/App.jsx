import "./App.css";
import Form from "./components/Form";
import Header from "./components/Header";
import Models from "./components/Models";
import { LoadingContext } from "./context/context";
import { useState } from "react";

function App() {
  const [loading, setLoading] = useState(false);

  return (
    <main>
      <div className="main">
        <div className="gradient" />
      </div>
      <div className="app">
        <Header />
        <LoadingContext.Provider value={[loading, setLoading]}>
          <Form />
          <Models />
        </LoadingContext.Provider>
      </div>
    </main>
  );
}

export default App;
