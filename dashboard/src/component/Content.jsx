import React, { Component } from "react";
import axios from "axios";
import { Drawer } from "antd";

import ProblemCard from "./ProblemCard";
import DrawerContent from "./DrawerContent";
class Content extends Component {
  state = {
    data: {},
    keys: [],
    selected: null,
    visible: false,
  };
  update = false;
  componentDidMount() {
    axios.get("http://localhost:3001/problems").then((data) => {
      this.setState({ data: data.data, keys: Object.keys(data.data) });
      console.log(data.data);
    });
  }

  onClose = () => {
    this.setState({ visible: false, selected: null });
    this.postData();
  };
  onCardClick = (key) => {
    this.setState({ selected: key, visible: true });
    this.update = false;
  };
  handleKeyUp = (e) => {
    let { selected, keys } = this.state;
    let index = keys.indexOf(selected);
    if (!selected) return;
    if (e.key === "ArrowRight") {
      index++;
      selected = index >= keys.length ? keys[0] : keys[index];
    } else if (e.key === "ArrowLeft") {
      index--;
      selected = index === -1 ? keys[keys.length - 1] : keys[index];
    }

    if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
      this.postData();
      this.setState({ selected });
    }
  };

  handleTextChange = (e) => {
    const { data, selected } = this.state;
    data[selected].correct_text = e;
    this.setState({ selected });
    this.update = true;
  };

  postData = () => {
    if (!this.update) return;
    const { data, selected } = this.state;

    if (!selected) return;

    const obj = data[selected];

    axios
      .post("http://localhost:3001/problems", {
        body: {
          ...obj,
        },
      })
      .then((e) => {
        this.update = false;
      });
  };

  render() {
    const { data, keys, visible, selected } = this.state;
    return (
      <div
        onKeyUp={(e) => this.handleKeyUp(e)}
        style={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}
      >
        {keys.map((key) => {
          const { image_path, image_name } = data[key];
          return (
            <div onClick={() => this.onCardClick(key)} key={key}>
              <ProblemCard
                path={image_path}
                title={image_name}
                description={""}
              />
            </div>
          );
        })}
        <Drawer
          title={data[selected] ? data[selected]["image_name"] : ""}
          height={460}
          closable={true}
          onClose={this.onClose}
          visible={visible}
          placement={"bottom"}
        >
          <DrawerContent
            dataSelect={data[selected] || {}}
            handleTextChange={this.handleTextChange}
          />
        </Drawer>
      </div>
    );
  }
}

export default Content;
