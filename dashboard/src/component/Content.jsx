import React, { Component, Fragment } from "react";
import axios from "axios";

import ProblemCard from "./ProblemCard";
class Content extends Component {
  state = {
    data: {},
  };
  componentDidMount() {
    axios.get("http://localhost:3001/problems").then((data) => {
      this.setState({ data: data.data });
    });
  }
  render() {
    const { data } = this.state;
    return (
      <Fragment>
        {Object.keys(data).map((key) => {
          const { image_path, image_name } = data[key];
          return (
            <ProblemCard
              key={key}
              path={image_path}
              title={image_name}
              description={""}
            />
          );
        })}
      </Fragment>
    );
  }
}

export default Content;
