The making of the protocol file, the connection with Kortex API, the SDK start up, and the actual task. These should be standartized and an AI should put a summary of the code that does them  and a skill that allows users to make studies that subscribe to our set up fast and reliably. 

# Lys Portal (the portal)
The Portal is a web-app that allows our players to collect data with ease. It holds the UI component of interacting with out python backend and running the tasks we give. It has to be very light and


## So what actually happens when we collect data irl? Problem:

``` mermaid
 timeline  
    title Data Collecction timeline irl & code 
    
    Flow2 started : Flow2 launched irl
    Recording started : In Kernel portal, user presses Start Recording 
					  : Data starts coming in
    Task script launched : In terminal, user starts activity/task script  
						: start_experiment marker to Kortex, later in snirf 
    Intro - Participant input : QT/instruction screen prompts for participant number  
    Intro - Session created : Session folder created  
		                    : Protocol file / Lys log created 
		                    : Logged creation date 
  
    Session start(New) : start_session marker, later in snirf
                  : Logged to Lys  
                  : Sent to Kortex  
  
    Intro end : intro_end  
              : Additional selected info written in file header comment  
              : Logged to Lys  
  
    Baseline : baseline_start  
             : baseline_end  
             : Logged to Lys  
  
    Task : Task events logged to Lys  
  
    Experiment end : end_experiment  
                   : Logged to Lys  
                   : Sent to Kortex

```
Note to figure:  the SKD commands are missing 


Good:
This ensures maximal information about participant's behaviour for data quality (QC) purposes, ability to standartize across paradigms and make task making easier as this order template will be enforced by the task.py and task_executor.py in abstract_interfaces. 
aka we can track how long participants take to enter the game/task and to choose their activity and etc. 

Bad: 
Makes it a bit unintiutive as we will not have an exact log of start_experiment (instead now we will at least have start_session when we can first record (prt file is made)). 
In the jsonl protocol file often it might go: comment entry comment entry in the first few lines as log and thats a bit weird


**As of now, we send start_experiment marker sometimes in step 3 or 5, sometimes there is intro or there isnt sometimes there is baseline or there isnt. So we handle in protocol.py object or preprocesor.py or live when using data in analysis**

#### What is it that costing us?
Confusion, hard to make quality checks, slow data turn over as manual labor involved, potentially losing some percent of data, hard to test and remake new tasks as no standard exsist and AI loves standard.

#### What is it going to cost us to implement solution? 
1) the code for the new task model is executed and the tasks are remade and retested to create the new prt files - 2 days probably (in prt_standartization github you can find this in part implemneted up to zork and percieved speech to be tested)  and then options:
2) OPTION A: Keep all existing code in main as is, all branch code and just add the new prt reader in the protocol.py I/O or somewhere else so that the code can go and try to read the prt no matter when it was created and just align the files. offer a standard input into 
	1) Implement QC checks based on the previous ones and heuristics + the future ones and be done with it -2 more days
3) OPTION B: rewrite all prt files while keeping the original in the folder, go over in main change all currently there analysis to work only with one type of Brain data-text pairing of type and have them all expect and then do it for all branches of analysis to be merged in main :) - pain and ? days --> we can say this goes to [[Data Analysis Procedure]] 
detail from [[Anon org]] we need to remake a lot of protocols anyways bcs they break stuff

# What does the QC entail?
On this level QC consists of dealing with the raw collected data and all components necessary to call it a successful trial. 
We need to check:
1. Sessions exist, files are downloadable, prt.jsonl file is made and if necessary processed ( maybe that happens later)
2. That they have finished downloading and that SDK chuncks are present
3. That both the prt file and the snirf files have session and end_experiment markers, and are of similar durations 
4. that there is a start experiment market in the kortex (extra)


### Behavioural QC
5. Check length between start of fnirs recording, start_experiment and session_start markers
6. & report:
	1. 2-1 = how long it takes for them to run the script
	2. 3-2 = how long it takes for them to select stuff and write stuff
	3. If any > 60 s FLAG and output actual time in daily_update ? 
7. Check if significant motion artifacts (either model or kortex or both)
8. Check if any weird events reported by kernel or us - broad I know 
9. Check if anything written in the #notes of the protocol file (NEW)
10. 