import React from "react";
import { useState, useEffect, useContext } from "react";
import io from "socket.io-client";
import { LoadingContext } from "../context/context";
import { circlesLoop } from "../assets/assets";

const socket = io("http://localhost:5000");

export const Models = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useContext(LoadingContext);

  useEffect(() => {
    socket.on("response", (data) => {
      setData(data);
      setLoading(false);
      console.log(data);
    });

    return () => {
      socket.off("connect");
      socket.off("message");
    };
  }, []);

  const getHighestScore = (response) => {
    let maxScore = 0;
    let bestModel = null;

    for (const model in response) {
      if (response[model].score > maxScore) {
        maxScore = response[model].score;
        bestModel = model;
      }
    }

    console.log(bestModel);

    return bestModel;
  };

  const bestModel = getHighestScore(data);

  return (
    <section>
      {loading ? (
        <img src={circlesLoop} className="loading" />
      ) : data ? (
        <div className="flex flex-row gap-5 m-10">
          <div
            className={`summary_box .gradient-border ${
              "ChatGPT3" == bestModel && "best-response"
            }`}
          >
            <h1
              className={`font-satoshi font-bold text-xl ${
                "ChatGPT3" == bestModel ? "text-black" : "orange_gradient"
              }`}
            >
              ✦ ChatGPT-3 Turbo
            </h1>
            <br />
            <p
              className={`font-inter font-medium text-sm ${
                "ChatGPT3" == bestModel ? "text-black" : "text-white"
              }`}
            >
              {data && data["ChatGPT3"] ? data["ChatGPT3"]["response"] : ""}
            </p>
          </div>
          <div
            className={`summary_box .gradient-border ${
              "ChatGPT4" == bestModel && "best-response"
            }`}
          >
            <h1
              className={`font-satoshi font-bold text-xl ${
                "ChatGPT4" == bestModel ? "text-black" : "orange_gradient"
              }`}
            >
              ✦ ChatGPT-4
            </h1>
            <br />
            <p
              className={`font-inter font-medium text-sm ${
                "ChatGPT4" == bestModel ? "text-black" : "text-white"
              }`}
            >
              {data && data["ChatGPT4"] ? data["ChatGPT4"]["response"] : ""}
            </p>
          </div>
          <div
            className={`summary_box .gradient-border ${
              "llama" == bestModel && "best-response"
            }`}
          >
            <h1
              className={`font-satoshi font-bold text-xl ${
                "llama" == bestModel ? "text-black" : "orange_gradient"
              }`}
            >
              ✦ Llama Chat
            </h1>
            <br />
            <p
              className={`font-inter font-medium text-sm ${
                "llama" == bestModel ? "text-black" : "text-white"
              }`}
            >
              {data && data["llama"] ? data["llama"]["response"] : ""}
            </p>
          </div>
          {/* <div
            className={`summary_box .gradient-border ${
              "falcon" == bestModel && "best-response"
            }`}
          >
            <h1
              className={`font-satoshi font-bold text-xl ${
                "falcon" == bestModel ? "text-black" : "orange_gradient"
              }`}
            >
              ✦ Falcon 40b
            </h1>
            <br />
            <p
              className={`font-inter font-medium text-sm ${
                "falcon" == bestModel ? "text-black" : "text-white"
              }`}
            >
              {data && data["falcon"] ? data["falcon"]["response"] : ""}
            </p>
          </div> */}
        </div>
      ) : (
        <div></div>
      )}
    </section>
  );
};

export default Models;
