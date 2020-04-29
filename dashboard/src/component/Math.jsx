import React from "react";
import MathJax from "react-mathjax";

const Math = ({ latex }) => (
  <MathJax.Provider>
    <MathJax.Node formula={latex} />
  </MathJax.Provider>
);

export default Math;
