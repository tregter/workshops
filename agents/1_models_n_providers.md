# Models & Providers


                   _,,jpygQQQQQQQQQQQQQQQQQyQ4(4
               jyQQQQQQQQQQQQQMQQQQQQQQQQQQQQQQ4
            ,pQQQQMMQMMMCCCC44444(MQMMMQQQQQQQQQ
           (QQQQQ(C444^ ~     44{<44(4((4M0MQQQQf
          (QQQQM`         ,4p44p(44<< 4<44((QQQQQ(
          QQQQM`        444Q([4M4<(((y4((4C44GQQQ4.
          QQQQ$      .(4(p(4(((4<,(<(4(4   .4(QQQQQp.
         QQQQ4(    .4QQQQQQQQ44pQQQQQQQQ#Q44(QQQQQQQQ(
         QQQQ(4.  ,pQQQQQQQQQQQQQQQMQQQQGGGGQQQQQQQQQQC,
         pQQQ[4   4QQQQQQQQQQQQQQQQQQQQ(4((((4QQQQQQQQQQ,
        44GGMC(  <GQ=QQQQQQQQQQQQQQQQQ4(((((((4((t(($QQQQC.
        44(((((. .GQQQQQQQQQQQQQQQQ0(((((((444<((4C44(0QQC.
       <C4C4(444.<4(t4GMQQQQQQQQQ004((4(44(44C4(<<..444MQQ(.
       .4(Q(4444. (p<<<<4Q4QQQQ[((4`  ..., ~4~ <4..`444GQQQ,
    ~_,4QQQG444<4 (((44444(QG4(4.   .44((44..   .. 4444GQQQQ4
     `4QQQQM444.444(44M((C(QQG4.  ,pp(((.<~~   ..  44444QQQQQ4
    .pQQQQ0[4444  ` .   _jWpQ[4 ,(",,        ....    (4QQQQQQQQQ[
    jQtMM$$Q((4(j4pp(((4QQQQQ((44([t(4. . 444.... .   4MQQQQQQQQQ,
   jQGQQg44(((4 pQQQQQQQQQQQQ4444(tQGpGpQ4444.~.<.    4QQQQQQQQQQ4.
   40pQQQQ(4<   OQQQQQQQQ0Q0$(4.4(4QQQQM((444  <..    4QQQQQQQQQQQy,
   44(QQQ$4(,.  ((QQQQQMQ(44`   44pQQQ44444  ...      jQQQQQQQQQQQQQ4
    4Qt4((444.  ((4QQQQQQpp(,     GQQ$(44C  ...      .<QQQQQQQQQQQQQC
     ((44444.   4(4QQQQQQMMQQ$(44((4((4C.   ..     ..(4QQQQ0QQQQQQQQ(
      4[(<,,,.   (((044C`````````<<((444....       4jQQQQM0QM[(44QQQ4
       4(4.`     ((G[(p.<44<<,. . ,4(((4.   ..    44QQMM44((((4((pQQ(
       <((       `[4$44((,``....,((((4444..       ((((C444444C44(Q$4
        4444,     4(t4QQQ44((<(4444((4<<  ..      .~~  ..C44<44(4(4
        44<4<4<j#4CC(44QQQQQQpt(((44.C  .       .          .44(tC,
        44444 ~<Q4&( `((4((((((44<~             |.(       .44(4QB.
        4C44C444Q444  4(.~`~<                   (.,      <444(QQQ.













------------------------------------
# What is an LLM?

->  I am not smart enough to answer that question
->  But this guy is: 3Blue1Brown
    ->  Large Language Models explained briefly
    ->  https://www.youtube.com/watch?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&v=LPZh9BOjkQs&feature=youtu.be

















                              ┌─────────────────┐                                  
                              │                 │                                  
┌──────────────────────┐      │                 │      ┌──────────────────────────┐
│                      │      │                 │      │                          │
│    Wordies go in     │─────▶│       LLM       │─────▶│  Other wordies come out  │
│                      │      │                 │      │                          │
└──────────────────────┘      │                 │      └──────────────────────────┘
                              │                 │                                  
                              └─────────────────┘                                  


->  This is our Axiom [*1]




















->  "But can't the agent just...?"
->  "Wordies go in, other wordies come out." Everything else is up to us.


















## Model Landscape

->  Gemini
->  Claude
->  GPT
->  Deepseek
->  Titan
->  Qwen













------------------------------------
# Where do LLMs live?


->  They usually run in the cloud
->  The people who host the models are called Model Providers
    ->  AWS Bedrock
    ->  GCP
    ->  Deepseek
    ->  Azure
    ->  OpenAI
    ->  Anthropic
    ->  X
    ->  Meta
->  Can I run it on my laptop though?

















->  My Macbook is an M1 Max 32GB
->  deepseek-r1:671b requires about 450GB of memory to run
->  After OS memory has been loaded, we get 450/26 approx 17 Macbooks


->  But we can run smaller models, like deepseek-r1:8b
->  Let's play with Ollama













------------------------------------
# Let's build some stuff


-> [Ollama Docs](https://docs.ollama.com/api/introduction)



















------------------------------------
# Covered

->  calling an LLM
    ->  invoke / generate
    ->  chat / messages
->  context
    ->  simulated memory
    ->  simulated tool calls
