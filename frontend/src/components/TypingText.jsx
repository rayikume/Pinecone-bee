import React, { useState, useEffect } from "react";

const TypingText = ({ text, speed }) => {
  const [displayedText, setDisplayedText] = useState("");
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (index < text.length) {
      const timeoutId = setTimeout(() => {
        setDisplayedText(displayedText + text[index]);
        setIndex(index + 1);
      }, speed);

      return () => clearTimeout(timeoutId);
    }
  }, [index, text, displayedText, speed]);

  return (
    <span>
      {displayedText}
      {index < text.length && <span className="cursor">|</span>}
    </span>
  );
};

export default TypingText;
