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
        style={{ width: "100%", maxWidth: "750px", direction: "rtl" }}
        rows="4"
      ></textarea>
    </Row>
    <Row justify="center">
      <textarea
        disabled
        style={{ width: "100%", maxWidth: "750px" }}
        rows={4}
        size="large"
        value={dataSelect["ocr_text"]}
      />
    </Row>
    <Row justify="center">
      <Card  style={{width:"100%",maxWidth: "750px"}}>
        <ReactJson src={dataSelect["nlp_mahrous_correct_text"]} />
      </Card>
    </Row>
    
    {/* <Row justify="center">
      <Card  style={{width:"100%",maxWidth: "750px"}}>
        <ReactJson src={dataSelect["nlp_mahrous_ocr_text"]} />
      </Card>
    </Row> */}

        
    <Row justify="center">
      <Card  style={{width:"100%",maxWidth: "750px"}}>
        <ReactJson src={dataSelect["solve"]} />
      </Card>
    </Row>
    <Row justify="center">
      <Card  style={{width:"100%",maxWidth: "750px"}}>
    {dataSelect["solve"] &&dataSelect["solve"].map((item,index)=>{
      return (
        <div key={index}>
          {Object.values(item).map((e,index2)=>e.map(ee=>ee.map(eee=>{
         console.log(ee)
            if(eee.type=='text') 
            return <p style={{textAlign:"right"}} key={`${index}_${index2}`}>{eee.value}</p>
            return <Math key={`${index}_${index2}`} latex={eee.value.slice(2,-2)}/>
    })))}
        </div>
      )
    })}
    </Card>
    </Row>



    

  </Fragment>
);

export default DrawerContent;
