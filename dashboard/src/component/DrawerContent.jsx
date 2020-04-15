import React, { Fragment } from "react";
import { Row, Input } from "antd";

const { TextArea } = Input;

const DrawerContent = ({
  image_path,
  ocr_text,
  handleTextChange,
  correctText,
  dataSelect,
}) => (
  <Fragment>
    {console.log(ocr_text, correctText)}
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
  </Fragment>
);

export default DrawerContent;
