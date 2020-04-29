import React, { Fragment } from "react";
import { Row, Card } from "antd";
import ReactJson from "react-json-view";
import Math from "./Math";
const DrawerContent = ({ handleTextChange, dataSelect }) => (
  <Fragment>
    <Row justify="center">
      <img
        src={dataSelect["image_path"]}
        alt=""
        style={{ maxWidth: "600px" }}
      />
    </Row>
    <Row justify="center">
      <textarea
        onChange={(e) => handleTextChange(e.target.value)}
        name=""
        value={dataSelect["correct_text"]}
        id=""
        style={{ width: "100%", maxWidth: "600px", direction: "rtl" }}
        rows="4"
      ></textarea>
    </Row>
    <Row justify="center">
      <textarea
        disabled
        style={{ width: "100%", maxWidth: "600px" }}
        rows={4}
        size="large"
        value={dataSelect["ocr_text"]}
      />
    </Row>
    <Row justify="center">
      <Card title="mahad nlp ocr" style={{ width: 300 }}>
        <ReactJson src={dataSelect["nlp_mahad_ocr_text"]} />
      </Card>
      <Card title="mahad nlp correct" style={{ width: 300 }}>
        <ReactJson src={dataSelect["nlp_mahad_correct_text"]} />
      </Card>
    </Row>
    <Row justify="center">
      <Card title="mahrous nlp ocr" style={{ width: 300 }}>
        <ReactJson src={dataSelect["nlp_mahrous_ocr_text"]} />
      </Card>
      <Card title="mahrous nlp correct" style={{ width: 300 }}>
        <ReactJson src={dataSelect["nlp_mahrous_correct_text"]} />
      </Card>
    </Row>
  </Fragment>
);

export default DrawerContent;
