import React, { Component } from 'react';
//import './home.css';
import Grid from '@material-ui/core/Grid';
import { withStyles } from '@material-ui/core/styles';
//import Paper from '@material-ui/core/Paper';
import CodeSearch from '../components/CodeSearch';
import CodePrice2 from '../components/CodePrice2';
import CodeChart2 from '../components/CodeChart2';


const styles = {
    root: {
        flexGrow: 1,
    },
    paper: {
        height: 140,
        width: 100,
    },
    control: {
        padding: 2,
    },
  };
  
  class CodeInfo2 extends Component {
    constructor(props){
        super(props);
        this.state = {
            selectedCode:"",
        }
    }
    componentDidMount(){
  
    }
    componentDidUpdate(prevProps, prevState){
  
    }
    handleSelectedCode = (selectedCode)=>{
        console.log("CodeInfo handleSelectedCode", selectedCode);
        this.setState({selectedCode});
    }
    render(){
        return(
            <div>
                <div>
                    <CodeSearch code={this.state.selectedCode} handleSelectedCode={this.handleSelectedCode} />
                
                
                    <Grid>
                        <Grid container justify="center">
                            <Grid key={"codePrice"} item>
                                <CodePrice2 code={this.state.selectedCode}/>
                            </Grid>
                            <Grid key={"codeChart"} item>
                                <CodeChart2 code={this.state.selectedCode}/>
                            </Grid>
                        </Grid>
                    </Grid>
                </div>
            </div>
        );
    }
  }
 /* const home = () => {
  
    return(
        <div>
            <h2>hello</h2>
        </div>
    )
}*/
  
  export default withStyles(styles)(CodeInfo2);