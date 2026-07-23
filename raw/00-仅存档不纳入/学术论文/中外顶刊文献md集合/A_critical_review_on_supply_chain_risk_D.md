# A_critical_review_on_supply_chain_risk_D

> **源文件**: A_critical_review_on_supply_chain_risk_D.pdf
> **页数**: 31

---

## 第 1 页

Author's Accepted Manuscript
A Critical Review on Supply Chain Risk –
Definition, Measure and Modeling
Iris Heckmann, Tina Comes, Stefan Nickel
PII:
S0305-0483(14)00125-X
DOI:
http://dx.doi.org/10.1016/j.omega.2014.10.004
Reference:
OME1441
To appear in:
Omega
Received date: 30 July 2013
Accepted date: 13 October 2014
Cite this article as: Iris Heckmann, Tina Comes, Stefan Nickel, A Critical Review
on Supply Chain Risk – Definition, Measure and Modeling, Omega, http://dx.doi.
org/10.1016/j.omega.2014.10.004
This is a PDF file of an unedited manuscript that has been accepted for
publication. As a service to our customers we are providing this early version of
the manuscript. The manuscript will undergo copyediting, typesetting, and
review of the resulting galley proof before it is published in its final citable form.
Please note that during the production process errors may be discovered which
could affect the content, and all legal disclaimers that apply to the journal
pertain.
www.elsevier.com/locate/omega

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 2 页

A Critical Review on Supply Chain Risk – Deﬁnition, Measure and Modeling
Iris Heckmanna,∗, Tina Comesb, Stefan Nickela,c
aDepartment of Logistics and Supply Chain Optimization, Research Center for Information Technology (FZI), Karlsruhe, Germany
bCentre for Integrated Emergency Management, University of Agder (UiA), Grimstad, Norway
cInstitute for Operations Research, Karlsruhe Institute of Technology (KIT), Karlsruhe, Germany
Abstract
Economic systems are increasingly prone to complexity and uncertainty. Therefore, making well-informed deci-
sions requires risk analysis, control and mitigation. In some areas such as ﬁnance, insurance, crisis management and
health care, the importance of considering risk is largely acknowledged and well-elaborated, yet rather heterogeneous
concepts and approaches for risk management have been developed. The increased frequency and the severe conse-
quences of past supply chain disruptions have resulted in an increasing interest in risk. This development has led to
the adoption of the risk concepts, terminologies and methods from related ﬁelds. In this paper, existing approaches
for quantitative supply chain risk management are reviewed by setting the focus on the deﬁnition of supply chain risk
and related concepts.
Keywords: risk deﬁnition, supply chain management, uncertainty, vulnerability, resilience, complexity
1. Introduction
Each process and decision in business is prone to uncertainty. Since wrong assessments and misjudgments may
lead to unforeseen developments, which may have important consequences when detected (too) late, uncertainties
need to be continuously monitored and managed. Along with the increasing number of relevant uncertainties, the
importance assigned to risk considerations has grown. In recent decades, we have observed this term being applied
to areas such as decision theory [75, 119], ﬁnance [63, 64, 92], actuarial science [82], health care [53, 77], marketing
[34, 120], management [90], emergency planning [33, 57, 60] and psychology [2, 20, 38].
Particularly in supply chain management many authors have felt the need to somehow capture risk. Due to the
increasing complexity and interrelation of modern supply chains, the type and nature of uncertain developments or
the impact of any action have become hard or even impossible to predict [58]. Additionally, major disruptions like
Hurricane Katrina, the piracy attacks offshore Somalia, global ﬁnancial crisis, ﬂoodings in Thailand, European ash-
cloud, Japanese earthquake and tsunami among others revealed a lack of preparedness of supply chain managers
towards uncertain developments in general [116].
∗Corresponding author
Email addresses: heckmann@fzi.de (Iris Heckmann), martina.comes@uia.no (Tina Comes), nickel@kit.edu (Stefan Nickel)
Preprint submitted to OMEGA
October 17, 2014

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 3 页

A close look into the use of the term risk in general and supply chain risk in particular reveals that its meaning is
far from clear. The Risk Response Network of the World Economic Forum among others have just recently identiﬁed
that more time and effort has to be invested not only in conceptual or methodical work but ﬁrst of all in the creation
of a common deﬁnition and understanding of supply chain risk [67, 117, 131, 135, 143].
This review overcomes a hole in the literature which regards the lack of a clear deﬁnition of risk within the
context of supply chain risk management. With the goal to provide a complete foundation of nowadays understanding
of supply chain risk, we studied not only mathematical approaches that originate from the operations research and
management science community, but also conceptual and empirical papers that provide managerial insights and risk
classiﬁcations. However, the main analysis sets the focus on the mathematical body of supply chain risk literature
and evaluates whether conceptual work has been transferred to mathematical approaches. Therein we reveal missing
aspects of prevailing supply chain risk deﬁnitions, quantiﬁcation measures and modeling approaches.
Since it is not possible to review all relevant literature, the analysis focuses on papers that either explicitly classify
and deﬁne supply chain risk or that quantitatively model risk for supply chain design and planning problems.
The remainder of this paper is organized as follows: the next section brieﬂy traces the development of the term risk.
By doing so, it will be easier to understand the motivation for the different deﬁnitions that are presented subsequently.
We focus on the use of risk in theory and practice, particularly the integration of risk management in corporate systems,
and existing risk management approaches, regulations and standards. Section 3 outlines existing concepts of supply
chain risk in research and practice. In Section 4, we derive important characteristics that drive today’s understanding
of risk. Presented as core concepts of risk consideration, these characteristics may also be used to deﬁne supply chain
risk. Section 5 provides a short discussion on measures that are used to quantify risk in the majority of analyzed papers.
The following section 6 reviews papers with regard to their modeling approach and solution techniques applied. The
conclusion and an outlook outlining ideas for future research are provided in Section 7.
2. The Evolution of Risk
In spite (or possibly because) of its long history, the term risk is still vague and often ill-deﬁned. Although in
everyday language the term is frequently used and easily understood [97], the underlying concepts are hard to deﬁne
and even harder to assess. The reason for the widespread, heterogeneous and inconsistent deﬁnitions of risk can be
traced back to its evolution, the continuous change of its nature, its meaning, and its purpose of use.
The origin of the word risk cannot be clearly determined, since this term seems to have roots in different cultures.
An etymological analysis of the European notion of risk leads to the Greek navigation term rhizikon, describing the
need to avoid “difﬁculties at the sea” [40]. Understood in this sense, the best approximation of the meaning of risk
would be fear or adventure. The former refers to commercial activities and implies physical and mental distress,
whereas the latter means pecuniary ventures as a strategy to engross the self-worth. In the 14 th century, when the
maritime trade between Northern Italian city states started to increase, traders adopted this perception and regarded
2

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 4 页

risk as the danger of losing their ships. For instance a spice merchant would think of potential situations that could
cause his ship to be lost: storms, piracy, mutiny of the crew, or diseases. Today, these ’what-if-stories’ are largely used
in planning and commonly referred to as scenarios [27]. They reveal potential developments and their consequences
[73]. However, the ultimate reason for the high risk of running a spicery business did not reside solely from external
events (such as storms or piracy), but also from the fact that the merchant usually owned only one ship – a single
supply channel – and all his capital had been invested in the goods transported by it. Because the consequences of
losing the ship were devastating for the merchant, his business was strongly vulnerable. The business of a merchant
who owned more ships or who additionally dealt in salt trade or had a commercial partnership – diversiﬁed business
risk – was less vulnerable. Such a merchant would have less reasons to be anxious. Within this context, risk expresses
the fear that economic activities lead to the loss or devaluation of an important asset or a decrease in the performance
of the business. Although the supply chains have become more complex, and are caught in a crossﬁre of a vast amount
of inﬂuences, today’s supply chain managers are essentially confronted with a similar situation to the merchants in the
16th century: In order to prevent their businesses from losing value, they need to identify alternatives, before or while
changes to their supply chain and its environment occur. The famous and much discussed example of supply chain
risk encountered by Nokia and Ericsson reveals, how the degree of preparedness leads to different outcomes [101].
Although these organizations had to deal with the same direct consequences of an unexpected incident, Ericsson
suffered deeply from a supplier shortfall possibly provoking them to leave the mobile market [101, 127, 129], while
Nokia could manage to acquire backup suppliers and alternative production capacities.
While the aforementioned understanding of risk is based on the fear of losing an investment, another view focuses
on the probability of events that result in loss. At the beginning of the 17 th century, risk became prominent in
mathematics, when Blaise Pascal (1623–1662) and Pierre de Fermat (1601–1665) started to measure uncertainty in
gambling [47]. Their work led to the development of Probability Theory, which still dominates the modern concept
of risk [16]. In fact, the connection between probability theory and risk has been observed since the 1950s and has
been applied to many research domains. As the performance of supply chains is becoming increasingly uncertain due
to unexpected changes, authors transferred this basic probability-based risk concept to supply chain risk management.
The probability of ﬂooding, earthquakes, and tsunamis in the Asian region, for example, make supplier shortfalls more
realistic and more threatening for supply chains as can be seen in a number of cases. However, less probable events
like ash clouds in European air space also demand for appropriate treatment.
Contributions in supply chain risk management mainly discuss the identiﬁcation of triggering-events and the
assessment of their probabilities of occurrence – although this risk perception might be limited for supply chains. The
more general concept of risk associated with the fear of losing (business) value has not evolved.
3

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 5 页

3. Existing Approaches of Supply Chain Risk Deﬁnitions
Although the topic is being considered as increasingly important, there are only a few authors explicitly deﬁning
supply chain risk. Those that do, found their deﬁnition on the assumption that supply chain risk is a purely event-
oriented concept. This risk perception is in accordance with the risk understanding developed over the last four
centuries that strongly relates risk to the probability of occurrence of disruptive events. In the context of supply chain
risk management, events are characterized by their probability of occurrence and their related consequences within
the supply chain. The reasons for the occurrence of risk (i.e., the initial or so-called triggering event) is not relevant in
this classiﬁcation: it can be found within one ﬁrm, within its supply chain or within the supply chain’s environment
[71]. While some authors analyze the consequences of an event for a single focal ﬁrm [151], others focus on the
performance of the supply chain as a whole [71], which can be affected by the occurrence of cascading effects that
propagate through the entire network.
Among the ﬁrst authors to establish a supply chain risk deﬁnition were March and Shapira: they deﬁne supply
chain risk as the “variation in the distribution of possible supply chain outcomes, their likelihood, and their subjective
values” [90]. Zsidisin provide a review of literature and industrial practices derived from case studies in order to
derive a deﬁnition of supply risk [162]. The author proposes a deﬁnition of supply risk that relates the occurrence of
an incident with the inability of the affected companies to cope with the consequences. His deﬁnition is adopted by
others as well [50, 78]. Much conceptual work has been provided by J¨uttner, Peck and Christopher. In a common
paper the authors deﬁne supply chain risk as “the possibility and effect of mismatch between supply and demand”
[67]. Likewise, Peck deﬁnes supply chain risk as “anything that [disrupts or impedes] the information, material or
product ﬂows from original suppliers to the delivery of the ﬁnal product to the ultimate end-user” [105]. However,
most conceptual research is dedicated to the categorizations of triggering events that are often synonymously referred
to as supply chain risk, which is often understood as a starting point for risk identiﬁcation [74], see discussion in
Section 4.
Figure 1 shows the result of the paper analysis with respect to the deﬁnition of supply chain risk. Note, we put the
emphasis of our analysis on the evaluation of mathematical-based models, therefore, references like [67, 90, 105, 162]
are missing in the Figure. Additionally, some of those papers have been selected for the analysis, although they do not
directly refer to supply chain risk, but provide valuable aspects for the quantitative modeling of risk in supply chain
problems. The majority of papers analyzed, however, miss to deﬁne supply chain risk, even though their emphases is
put on this topic.
Taking the above references into account, we conclude that the deﬁnitions of supply chain risk are often vague,
ambiguous and defy quantiﬁcation. As a result, supply chain risk is still difﬁcult to assess, monitor, control, and
hardly representable in mathematical decision models.
4

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 6 页

(B) No Explicit
Supply Chain Risk
Deﬁnition 82%
d) 52%
[111]
[7]
[125]
[44]
[37]
[153]
[62]
[43]
[124] [107]
[158]
[73]
[155]
[123]
[55]
[6]
[87]
e) 12%
[137]
[102]
[156]
[157]
f) 6%
[134]
[4]
g) 12%
[100]
[85]
[81]
[14]
(A) Explicit
Supply Chain Risk
Deﬁnition 18%
a) 9%
[159]
[26]
[86]
b) 6%
[50]
[78]
c) 3%
[79]
Figure 1: Analysis of supply chain risk deﬁnitions. Articles provide (A) explicit supply chain risk deﬁnitions and deﬁne risk as a) the probability
and adverse outcome, b) the supply risk by Zsidisin [162], or c) the deviation from the expected. Majority offers (B) no explicit supply chain
risk deﬁnition and imply risk to be d) an event, e) a deviation from the expected/objective, f) a probability, or g) provide no further insight to the
deﬁnition of risk.
4. Core Characteristics of Supply Chain Risk
So far, there is no unanimous deﬁnition of supply chain risk, but there is a vast amount of literature coming from
multiple domains dealing with risk. We chose the following domains to represent the most relevant streams of the
use of risk, although we acknowledge that there may be further deﬁnitions in other disciplines: ﬁnance, insurance,
decision theory, utility theory, emergency management and health, safety, environmental and reliability engineering.
Each of the following paragraphs outlines how risk is understood according to selected domains of application and
explains the underlying rationales.
Based on this analysis we identify core characteristics that drive nowadays supply-chain risk understanding: The
assessment of supply chain risk is closely related to the objectives that need to be accomplished by the underlying
supply chain. The degree of achievement of these objectives depends on the exposition of the underlying supply
chain towards unexpected and uncertain developments. Risk exposition is further classiﬁed by potentially disrupting
triggers, supply chain’s ability to handle irritations, and time-based aspects that align the occurrence of the disruptive
triggers to the current status of the supply chain. The signiﬁcance of a potential non-achievement of objectives is
assessed by the risk attitude of the decision maker. These characteristics are highlighted in Figure 2.
5

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 7 页

SUPPLY CHAIN RISK
RISK EXPOSITION
RISK-AFFECTED
OBJECTIVE
Efﬁciency
Effectiveness
RISK ATTITUDE
Aversion
Seeking
Neutrality
TIME-BASED CHAR-
ACTERISTICS
DISRUPTIVE TRIGGERS
Triggering Event
Probability
AFFECTED SUP-
PLY CHAIN
Vulnerability
Resilience
Figure 2: Core Characteristics of Supply Chain Risk
4.1. Objective-driven Risk
Risk considerations are very popular in ﬁnancial management. The aim of this area is to efﬁciently plan, monitor,
and control the capital resources of a company. Financial risk management seeks to predict and to handle uncer-
tain developments, which may lead to a degradation of company’s value and forestall the achievement of corporate
objectives. In ﬁnance, risk is measured as ﬂuctuations around the expected value of ﬁnancial returns. Originally,
researchers considered the use of mathematical models for ﬁnding decisions which could capture this perspective of
risk. In the initial models, mean-variance objective functions were considered, see for instance [39] and [91]. In
ﬁnance, the understanding of risk comprises both gains and losses. Several characterizations of ﬁnancial risk subsist,
most of which distinguishing market, credit, currency or liquidity risk. These risks describe the potential for losses
due to movements in market prices, debt payments, exchange rates, and interest in trading certain assets, respectively.
Financial risk management models attempt to predict consequences of the aforementioned movements. In contrast to
the aforementioned risks it is by far more difﬁcult to identify, model and assess ﬁnancial losses due to operational
risk. Operational risk is deﬁned by the Basel II Committee as “the risk of loss resulting from inadequate or failed
internal processes, people and systems or from external events” [11, p.137]. In order to determine adequate capital
reserves that serve as fall back positions when operations fail, organizations need to fully understand the interrelated
consequences and dynamics that occur with operational risk. Operational risk better reﬂects the complexity, uncer-
tainty and diversity of risk sources that are valid for supply networks. It provides, therefore, a better conceptual basis
for the notion of supply chain risk than ﬁnancial risk as it is understood for market, credit, currency and liquidity risk.
The discussion shows that ﬁnancial risk management is concerned with risk that refers to deviations of expected
monetary objectives. Similarly, supply chain management has a signiﬁcant inﬂuence on business goals and therefore
provides competitive advantage, when designed appropriately in regards to meet business objectives [151]. However,
in supply chain management goals can be achieved in two ways: efﬁciently or effectively [61, 96]. While effectiveness
6

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 8 页

means that achieving a predeﬁned goal can be guaranteed even if conditions are adverse, efﬁciency refers to minimal
spending of resources to reach this goal. The primarily purpose of a supply chain is to satisfy customer’s demand,
the availability of resources and the functionality of supply chain processes, therefore, needs to be guaranteed. The
effectiveness in the context of supply chain management includes these aspects [19]. In contrast, purely efﬁciently
designed supply chains provide the possibility of higher competitive advantages. Supply chain efﬁciency refers to a
cost- and waste-minimal execution of supply chain activities [19]. The recent series of reported supply chain failures
has shown that when efﬁciency is the sole objective, there is little buffer to enable continuity or recovery in the event
of a disruption. It seems that the pursuit of efﬁciency and effectiveness are conﬂicting ([78]) and need to be carefully
balanced.
Stock and Boyer developed a consensual deﬁnition of supply chain management that incorporates the aforemen-
tioned thoughts [138]. According to the authors the management of supply chains seeks to plan, monitor, and control
a network of interdependent organizations that facilitates different types of ﬂows between the original producer to
the ﬁnal customer with the objectives to maximize proﬁtability through efﬁciencies as well as to achieve customer
satisfaction [138]. Consequently, a deﬁnition of supply chain risk should reﬂect the potential non-achievement of
corporate goals due to ineffective or inefﬁcient supply chain processes. Meanwhile, most approaches concentrate on
reducing monetary or ﬁnancial consequences of uncertain and unexpected developments. Only a few authors con-
sider effectiveness-based aspects like service level. Kull and Closs for instance use discrete-event simulation with
the objective of increasing customer satisfaction [78]. Zsidisin deﬁnes supply risk and relates the occurrence of an
event to the inability of the supply chain to satisfy customer’s demand [162]. Fewer authors combine both concepts in
order to truly balance supply chain efﬁciency with supply chain effectiveness. Peng et al. develop a system dynamics
model for balancing inventory level and service level [107]. The majority of approaches, however, focuses on a purely
efﬁciency-based representation: when effectiveness is considered, it is measured in terms of the sighted efﬁciency
ﬁgure (costs or proﬁt). Figure 3 presents main results of this analysis with regard to the mathematical approaches
considered.
4.2. Risk Exposition
Besides the objectives set to the supply chain, the exposition towards unexpected or uncertain developments have
meaningful inﬂuence on how supply chain risk is understood. The risk exposition is speciﬁed by the occurrence of
a so called-triggering event, as well as by characteristics of the underlying supply chain. While the former is further
speciﬁed by the probability of occurrence and the effect within the supply chain, the latter is described by concepts
like vulnerability or resilience. Additionally, time-aspects need to be considered when referring to disruptive triggers
and the preparedness of the affected supply chain.
Disruptive Triggers
A disruptive trigger is further speciﬁed through the concepts of probability and event.
7

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 9 页

(A) Efﬁciency 42%
[50]
[111] [125]
[62]
[100] [158]
[85]
[26]
[81]
[102]
[55]
[79]
[86]
[153]
(B) Efﬁciency and efﬁciency-based
Effectiveness 46%
[44]
[37]
[137]
[43]
[4]
[124] [155]
[134] [123]
[14]
[156]
[7]
[6]
[87]
[157]
(C) Balancing Efﬁciency
and Effectiveness 3%
[107]
(D) None 6%
[73]
[159]
(E) Effectiveness 3%
[78]
Figure 3: Supply Chain Risk Objectives: (A) The predominantly objective is optimizing efﬁciency-based ﬁgures like costs, proﬁt, or inventory.
(B) When effectiveness is considered it is transferred to efﬁciency-based objectives by the means of penalty or shortage cost for unmet demand.
(C) Efﬁciency and effectiveness balancing as well as (E) pure effectiveness-based approaches are limited. (D) Some work may serve for different
risk-objectives.
Probability. The central aspect of risk perception in most research areas is the availability of probability distribu-
tions. Decision theory, for instance, aims to support decision-makers in the construction or identiﬁcation of an optimal
or at least a satisﬁcing decision. This is difﬁcult in complex situations, when the assessment and evaluation of the
consequence of decision is affected by different types of uncertainty [32, 46]. The effective and efﬁcient practice of
supply chain management in today’s globalized world depends on the collaboration between geographically dispersed
organizations [76]: (local) information must be collected, evaluated and shared across organizational boundaries [48].
Rosenhead et al. were the ﬁrst to classify a decision process according to the available information into three cate-
gories: certainty, risk and uncertainty [119]. Under certainty all parameters are deterministic and known. The relation
between information (input) and the decision (output) is unambiguous. Situations that are not certain comprehend
some kind of fortuity. Reasons for the need to make decisions under these circumstances vary from lacking time and
resources to collect, process and evaluate information to the inherent complexity of systems that forestalls predicting
the consequences of a decision [32, 59, 84, 161]. To distinguish between these fundamentally different situations, two
categories are introduced: decision making under risk relies on probability distributions, which govern the relation
between input and output. Decision making under uncertainty needs to be made despite the lack of information about
the likelihood of parameter changes.
Most authors adopted this categorization and refer supply chain risk to the extent of information availability about
randomly changing supply chain parameters – assuming probability speciﬁcations are at hand. Yet information pro-
8

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 10 页

cessing needs to respect the fact that the situation, its development and the information about both may be uncertain,
fast-changing and with varying degrees of relevance and reliability. Still supply chain managers need to make deci-
sions even when no information about the type of fortuity is available. Supply chain risk therefore addresses both
decision making under risk and under uncertainty.
The type of fortuity used to describe the development of uncertain parameters is depicted by uncertainty models.
The literature analysis follows the categorization of Owen and Daskin [103]. The authors distinguish between proba-
bilistic approaches and scenario planning approaches. While the former explicitly consider probability distributions,
the latter evaluate generated sets of possible future values, which can be weighted by discrete probability values, but
do not have to [103]. Table 1 shows the results of this analysis.
Uncertainty model
Reference
Share
Probabilistic Approach
[7] [37] [43] [155] [159]
22%
Scenario Approach
[4] [6] [7] [14] [50] [55] [62] [79] [87] [102] [111] [123] [124] [125]
[134] [137] [156] [157]
78%
Table 1: Uncertainty model of uncertain parameter development
Triggering Event. The strong relation between the concepts of probability and risk is adopted by health, safety,
environmental (HS&E) as well as by reliability engineering. However, a new aspect is emphasized by the implication
that risk is understood as an event or a series of events. The international engineering standard ISO14971 deﬁnes
and measures a risk R as the product of probability and harm of an event e: R = P eSe, where Se and Pe refer
to the severity and probability of e respectively [1]. Most of today’s supply chain risk deﬁnitions start from the
assumption that events are the decisive factor determining risk [154]. Consequently, huge efforts are invested in
gathering, analyzing and assessing information to control potential triggering events that could materialize supply
chain risk. To assess supply chain risk, triggering events are modeled as a function of their severity in terms of
impact on the supply chain goals and their frequency of occurrence. Different terms are often used synonymously
to refer to triggering events, e.g. disturbance [141], disruption [128], disaster [139], hazard or crisis. According to
Svensson a disturbance is a “random quantitative or qualitative deviation from what is normal or expected” [141]. A
negative consequence of disturbance is related to “a deteriorated goal accomplishment in terms of economic costs,
quantitative deviations [...] and qualitative deviations”. Wagner and Bode state that a disruption is characterized by
its probability, severity and effects [151]. A disruption is further described as a combination of the triggering event,
which is characterized through frequency of occurrence and magnitude, and a consequential situation, which threatens
the normal course of business operations. A disruption is regarded as more severe and often persist for a longer period
in time than a disturbance.
Klibi and Martel combine the availability of probability information and the extent of impact related to each
triggering event. The authors distinguish between random, hazardous, and uncertain events. The former are described
by probability distributions and occur within single periods. Hazardous events affect supply chain’s performance in
9

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 11 页

adjacent periods. They are considered to be rare but repetitive. No probability information is available for uncertain
events, however, they are considered to have enormous impact on the supply chain in adjacent periods [73].
As supply chain risk is understood as a triggering event, most authors focus on categorizing supply chain risk
with regards to the triggering events in order to distinguish it from other business risks [151]. This serves to better
understand and manage its inherent diversity. While the majority of the approaches relate supply chain risk to the
source or root causing the deviations, some authors relate risk to ultimate consequences. According to J¨uttner et al.
and Kaj¨uter these approaches distinguish between cause- and effect-oriented deﬁnitions of supply chain risk [67, 70].
Major efforts in the Anglo-American supply chain risk management literature have been dedicated to cause-oriented
methods. The rationale behind is that by knowing the cause, appropriate measures to reduce the likelihood of occur-
rence can be implemented. Additionally, the taxonomies differentiate between sources related to the supply network
and to supply chain processes. Table 2 shows a summary of relevant supply chain risk categories and subcategories
as deﬁned in literature.
In the following the focus is set to the analysis of risk sources. Depending on whether the risk source lies within
or beyond the supply chain boundaries, we ﬁnd endogenous and exogenous origins for the supply chain risk. As a
supply chain usually consists of several different interconnected companies, G¨otze and Mikus further distinguishes
endogenous risk sources as “beyond company borders” and “corporate-wide” sources [52]. Another classiﬁcation
refers to the possibility of controlling the risk: J¨uttner et al., Waters, and Wagner and Bode distinguish internal from
external risk sources that are beyond the managers’ control (e.g., policy or market risk) [67, 151, 154]. Christopher
and Lee, J¨uttner et al., and Christopher and Peck ﬁnd three different types of network related sources of supply chain
risk: lack of ownership, chaos, and inertia [29, 30, 67]. Lack of ownership refers to the increasing number of logistic
partners and the resulting unclear lines of responsibilities. The increased complexity of the supply network, signiﬁcant
changes in the environmental conditions, and market signals, drive inadequate mitigation [67], which result from
over-reactions or distorted information. Among others, process-related sources of supply chain risk are for example
referred to the Supply Chain Operations Reference (SCOR) model. Risk sources are assigned to the key processes
deﬁned within the SCOR model: plan, source, make, deliver, and return. Consequences of “SCOR-process-risks”
[160] are further characterized by quality, delay, breakdown, costs etc., to facilitate analysis and communication.
An alternative approach categorizes supply chain risk according to the area that is affected by the occurrence of
risk. Perspectives of this category refer to the basis of the extent, the controllability, or the network-wide location
of the impact. Kaj¨uter differentiates between cumulative, additive, and singular supply chain risks [69]. Cumulative
supply chain risks intensify as they propagate along the supply chain processes. Additive supply chain risks have
negative effects along the supply chain if they co-occur. Finally, singular supply chain risks are locally isolated, thus
not affecting any other parts of the supply chain. Tang provides a set of dimensions referring to the extent of impact by
addressing the risk level of certain events and differentiating between operational and disruption risks [144]. Simchi-
Levi focus on the role of decision-makers and provide two dimensions of analysis by distinguishing known-unknown/
unknown-unknown and controllable/uncontrollable risk [129, 130]. The ﬁrst dimension refers to the predictability of
10

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 12 页

Category
Subcategory
Perspective
Type of supply chain risk (characteristic of supply chain risk source)
Author
Risk sources
Network
Location
supply chain exogenous
[52]
beyond company borders supply chain endogenous
corporate-wide supply chain endogenous
supply
[68]
demand
environmental
supply chain network (physical network, ﬁnancial network, informational, relational, innovational network)
[24]
Controllability
internal
[67]
external
[154]
internal (demand side, supply side, regulatory/legal/bureaucratic, infrastructure, catastrophic),
[151]
external (regulatory/legal/bureaucratic, infrastructure, catastrophic)
lack of ownership
[29]
chaos
[67]
inertia
[30]
Assessment
quantitative
[140]
qualitative
Stakeholder
supplier-related (disruptions, delays, systems, information processing, intellectual property, procurement, receiv-
ables)
[28]
internal (disruptions, delays, systems, information processing, procurement)
customer-related (disruptions, delays, systems, information processing, receivables)
Process
SCOR levels
plan (quality, delay, breakdown, costs)
[160]
source (quality, delay, breakdown, costs)
make (quality, delay, breakdown, costs)
deliver (quality, delay, breakdown, costs)
return (quality, delay, breakdown, costs)
Controllability
environmental
[72]
supply
(intra-corporate) process
(intra-corporate) control
demand
Organizational functions
research & development
[80]
supply
production
distribution
ﬁnancial
personal
management
Logistical operations
order processing
[52]
inventory
warehouse
packing
transport
Target area of Risk
Location
corporate
[52]
supply chain wide
Extent of impact
operational (demand, supply and cost deviations)
[144]
disruption (natural and man-mad disasters)
Controllability
known-unknown/unknown-unknown
[130]
controllable/uncontrollable
Propagation
cumulative
[69]
additive
singular
Table 2: Supply chain risk categories
11

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 13 页

unknown events. The latter describes the ability to manage and limit frequency and impact of risk. The unknown-
unknowns are risks that can hardly be predicted. Terrorist attacks, epidemics, or geo-political instability are typical
examples, but due to the climate change, also extreme weather events and related natural catastrophes will become
harder to predict. The known-unknowns are risks that can be predicted from analyses of past events, for example by
the means of statistical data analysis, e.g. meantime to failure, supplier lead time [130]. Controllability refers to the
ability to manage and limit frequency and impact of risk. This classiﬁcation is subject to individual expert assessment:
the predictability and controllability of execution problems strongly depend on the nature of the business environment
and the sighted level of business objectives. Moreover, the binary character makes it hard to compare the degree of
control or knowledge between different events.
Based on these categorizations, Figure 4 shows those approaches that strongly differ between the source of uncer-
tainty and the affected area. For instance Goh et al. develop a stochastic model for a facility location and distribution
planning problem under supply, demand, and exchange rate risk, where uncertainty arises from supply, demand and
exchange rate, respectively [50]. Supply chain risk is regarded as the source of uncertainty. Similarly, Mak and Shen
as well as Sawik regard risk as the disruption risk, while the source of uncertainty is modeled as a distribution function
of the disruption [87, 124].
Other sources of uncertainty are referred to as supply risk [37, 43, 44, 78, 79, 86, 123, 125, 159], demand risk
[6, 14, 37, 50, 79, 111, 125, 134], or risk of (total) cost [6, 50, 155]. Most approaches, however, describe supply chain
risk as the deviation of the affected objective, which is most often proﬁt-, cost-, or cash-ﬂow-oriented and therefore
referred to as monetary ﬁgure [4, 7, 26, 55, 62, 81, 85, 100, 102, 125, 137, 156, 157, 158]. Minor work is dedicated
to regard risk as customer’s satisfaction [78] or supplier failures [153].
(A) affected area (50%)
monetary ﬁgure
[137]
[125]
[7]
[62]
[4]
[100]
[158]
[85]
[26]
[81]
[102]
[156]
[55]
[157]
customer satisfaction
[78]
supplier failure
[153]
(B) source (50%)
supply
[125]
[44]
[37]
[159]
[43]
[78]
[123]
[79]
[86]
demand
[50]
[111] [134]
[79]
[125]
[37]
[14]
[6]
cost
[50]
[155]
[6]
disruption
[124]
[87]
Figure 4: Literature analysis of supply chain risk categories: (A) Supply chain risk is classiﬁed upon the affected KPI and/or (B) supply chain risk
is understood as the source of uncertainty and therefore related to the uncertain parameters.
12

| n | [153] |  | [124] [87] | cost demand supply |
| --- | --- | --- | --- | --- |
|  | [78] |  | [50] [155] [6] |  |
|  | [7] [100] [26] [156] [125] [4] [85] [102] [157] [137] [62] [158] [81] [55] |  |  |  |
|  |  |  | [6] [14] [37] [125] [50] [111] [134] [79] |  |
|  |  |  | [43] [78] [123] [79] [125] [44] [37] [159] [86] |  |

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 14 页

Affected Supply Chain
From emergency management another dimension of risk exposition can be identiﬁed. To prevent harm from
human lives, to keep safety and to ensure sustainable growth, authorities and policy makers have sought to anticipate
and prepare for the unexpected [108, 148]. Examples include emergency management plans [5] or the design of
stress tests for critical infrastructures [113]. In these contexts, risk is often determined as a function of hazard,
vulnerability and exposure [22, 95]. This distinction is targeted at supporting decision-makers by distinguishing the
external components of risk that can hardly be inﬂuenced (such as a natural hazard) from the internal values that can
be controlled or manipulated [17]. This approach does not only regard risk as a threat deriving from triggering events,
but also as a concept that depends on characteristics of the underlying organization. Only some authors have recently
highlighted the correlation between magnitude of supply chain risk and the capability of resistance of the underlying
system [73, 86].
The concept used to describe the extent to which a supply chain is susceptible to a speciﬁc or unspeciﬁc risk
event is called supply chain vulnerability. It is remarkable that prevalent deﬁnitions of both triggering event and
supply chain vulnerability use concepts and computational formulae that are similar, often even identical, to supply
chain risk deﬁnitions. A concept closely related to supply chain vulnerability is supply chain resilience describing the
ability of a supply chain to overcome vulnerability. In general, vulnerability is deﬁned as a concept that describes “the
characteristics and circumstances of a community, system or asset that make it susceptible to the damaging effects
of a hazard” [147]. In this sense, supply chain vulnerability can be understood as a concept that comprehends the
supply chain as a system within its socio-economic environment comprising the abilities to respond to the hazard
and cope with the damage that could occur. Three main perspectives of deﬁnitions describing the concept of supply
chain vulnerability can be distinguished within the contemporary literature: deﬁnitions are either identical to the
deﬁnition of supply chain risk, or they relate to the extent of supply chain exposure or they refer to characteristics of
the underlying supply chain. Table 3 illustrates the prevailing perspectives on vulnerability.
Perspective
Deﬁnition of Supply Chain Vulnerability
Author
supply chain risk
Supply Chain Vulnerability = S ePe
[36]
[65]
[128]
“something is at risk; vulnerable: likely to be lost or damaged”
[105]
vulnerability as a construct consisting of two components, namely “disturbance” and
“the negative consequence of disturbance”
[140]
[141]
[142]
supply chain exposure
“propensity of risk sources and risk drivers to outweigh risk mitigating strategies”
[67]
“an exposure to serious disturbances, arising from risks within the supply-chain as
well as risks external to the supply-chain”
[25]
[30]
a susceptibility to incidents that can reduce availability of network resources
[8]
[15]
supply chain characteristics
“is a function of certain supply chain characteristics”
[150]
“incapacity of the supply chain to react to the disturbances at a given moment”
[10]
“characteristics and circumstances of a system [...] that make it susceptible”
[17]
[109]
[147]
Table 3: Supply chain vulnerability deﬁnitions
13

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 15 页

The ﬁrst perspective in Table 3 refers to the deﬁnition of supply chain risk: authors from the ﬁelds of supply
chain risk management, transportation systems and network analysis understand vulnerability as a combination of
the likelihood of a triggering event and its related consequence [36, 65, 128, 140, 141, 142]. Deﬁning supply chain
vulnerability as “something [that] is at risk” [105, p.132] requires an understanding of what is meant by supply chain
risk. Additionally, there is no clear and unanimous distinction between the deﬁnition and understanding of supply
chain vulnerability and supply chain risk.
Further work focuses on developing a conceptual and rather qualitative understanding of supply chain vulner-
ability by relating it for instance to propensity, susceptibility and exposure [8, 25, 30, 67, 150, 152]. A ﬁrst step
towards a systematic understanding of supply chain vulnerability was taken by Wagner and Bode [150]. Following
their argumentation certain structural supply chain characteristics can inﬂuence corporate loss given a supply chain
disruption. Similarly, Barroso et al. deﬁne supply chain vulnerability as the “incapacity of the supply chain to react
to the disturbances at a given moment, and consequently to reach supply chain objectives” [10].
The concept of resilience is applied in many different disciplines such as ecology, engineering, sociology, psy-
chology, economics and organizational analysis. The overall understanding of resilience relates to the ability of the
underlying system (material, network, individual, companies or corporate entities) to adjust or maintain essential
functions under stressful and harsh conditions. In engineering resilience refers to a material’s characteristic “to re-
cover its size and shape after the deformation caused by especially compressive stress” [94]. Particularly in crisis and
emergency management, resilience is often deﬁned as the response to an actual threat, the ability to “bounce back”
to the initial state [18, 33, 42, 89]. This state is considered as a point of reference, although its optimality is not
guaranteed. In fact, in many situations it can be advantageous to adjust to or strive to attain a new state. In supply
chain management, reasons may be that environment and operating conditions have changed in a way that turn the
initial state unfavorable, or because the supply chain has learned from the disruption and adapts to the new (desired)
state to improve preparedness. The ﬁrst deﬁnitions of resilience referring to supply chain management were devel-
oped in 2004 at the Cranﬁeld University [30] and in parallel studies at the MIT [128]. This work resulted in a ﬁrst
concise deﬁnition of supply chain resilience, which is still dominating: supply chain resilience is deﬁned as a supply
chain’s ability to return to its original or move to a new, more desirable state after being disturbed [30, 49, 105, 110].
While this understanding is uncontested in the supply chain management literature, different attitudes prevail about
how supply chain resilience is related to supply chain vulnerability and to supply chain risk and how supply chain
resilience can be achieved. Consequently, deﬁnitions on supply chain resilience either refer to the ability to overcome
supply chain vulnerability [10, 109, 140, 141, 142] or to the ability to reduce supply chain risk [42, 66, 104]. A
research analysis of current literature reveals dimensions, which are deemed to be important to increase supply chain
resilience. According to Rice and Caniato the most relevant “resilience capabilities” are ﬂexibility and redundancy
[114]. Both can be further speciﬁed through ﬂexibility-related concepts like agility [30], responsiveness [23], velocity
[66], or intra-corporate concepts such as supply chain risk management culture [30], collaboration [115] and visibility
[30].
14

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 16 页

Some conceptually oriented work has already described the need to combine the event-driven perception of supply
chain risk with a systematic-driven view on the underlying supply chain [66, 150]. Other quantitative works pointed
out the importance of combining disruptive triggers with the conﬁguration of the supply chain [73, 78, 86, 126], but
only a few applied this perception within their models, see for example [6].
Time-based Characteristics
A universal aspect of risk, which is applied in many different domains, is the consideration of time. In ﬁnancial
management, for example, the time horizon length has a meaningful inﬂuence on the assessment of risk and has
attracted much attention [21, 51]. In emergency or disaster management early warning systems yield to increase the
preparedness of a system with regard to reaction-time [112].
The literature on supply chain risk management has not yet considered in depth time-aspects, yet some authors
point out their importance with respect to the modeling of supply chain risk [55, 86, 88, 127, 151]. As can be derived
from the literature analysis, time-aspects are introduced for the modeling of disruptive triggers or for characterizing
the affected supply chain. The magnitude of consequences, for instance, depend on the current work load of the
affected supply chain (netting between demand quantity and available capacities). Considering the European ash
cloud in 2010, it is quite obvious that the consequences would have been less severe if the Icelandic volcano had
erupted during Christmas holidays, when many production facilities are closed anyway. The time of an impact is
important in the consideration of supply chain risk [14]. Time-based characteristics that describe the ability of the
affected supply chain to discover and respond to disruptive triggers are captured by Ben-Tal et al. as well as Sodhi
and Tang [14, 136]. The authors distinguish between time to design a solution in response to the disruption [14], time
to deploy the solution, and the time of recovery [136]. Besides characterizing the affected supply chain, time-based
aspects describe properties of a disruptive trigger. For example the speed of an event captures how fast parameters
change during or after the occurrence of an event [88]. The time for detection of an event formalizes the time until
information about the event are available [88, 136]. The frequency captures the time between two triggering events
[88]. The frequency of such events has increased considerably over the last years [31]. The duration of changes
evoked by triggering events are declared as a relevant temporal aspect [127, 151, 158].
However, the classiﬁcations of time-based characteristics are of conceptual nature and have not yet been fully
transfered to mathematical approaches. The description of time-based characteristics mainly relates to supply chain
modiﬁcations that were evoked by triggering events, and do not relate to decisions, risk management, and required
counter measures. Changes may also arise by uneventful trends or slightly varying level shifts. As the literature
analysis reveals, approaches have not payed much attention to time-based characteristics of supply chain risk so far.
Although mid-term problems like inventory, supply or demand planning imply the consideration of several periods,
they do not employ time for capturing risk.
15

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 17 页

4.3. Risk Attitude
Derived from utility theory and applied in the ﬁeld of ﬁnancial risk management, risk is speciﬁed by the risk
attitude of the decision maker. The subjective perception of the importance of risk is divided into three groups:
risk-averse, risk-seeking, and risk-neutral. These attitudes may drive managers’ decision-making processes and lead
to different solutions. Supply chain risk, as risk in general, may be regarded as a subjective concept that relies
on the individual’s assessment of potential outcomes, rather than an objective concepts [41]. Risk attitudes and
individual or organizational preferences, therefore, have a decisive inﬂuence on the measurement of future supply
chain performance and consequently co-determine supply chain decisions. While most of the approaches do not
explicitly consider different risk attitudes, some authors refer to subjective perceptions of the decision maker. Liu
and Nagurney, for instance, suggest that supply chain managers should ﬁrst evaluate the risk tolerance level of the
ﬁrm before making decisions that need to last for the long-run [85]. Wakolbinger and Cruz apply a weighting factor
representing an adjustable risk attitude of the decision maker [153]. Table 4 summarizes which of the analyzed
approaches considered risk attitudes explicitly within their models.
Ref
Single risk attitude
Multiple risk attitudes
risk-averse
risk-neutral
risk-seeking
adjustable
[6]
✓
[7]
✓
✓
[26]
✓
[55]
✓
[73]
✓
✓
[81]
✓
[85]
✓
✓
[87]
✓
[100]
✓
[102]
✓
[124]
✓
✓
[123]
✓
[125]
✓
✓
[137]
✓
[153]
✓
[155]
✓
[157]
✓
✓
Table 4: Risk attitudes considering approaches
Interestingly, risk-seeking attitudes are not considered in supply chain risk literature so far. A reason might be
that supply chain risk is mainly related to negative developments of supply chain objectives. However, to the best of
our knowledge, deﬁnitions of different attitudes towards supply chain risk do not exist in the contemporary literature.
As deduced in Paragraph 4.1, the extent of supply chain risk strongly depends on pursued goals of the underlying
supply chain. Supply chain goals are detailed by the type of objective, which can be both efﬁciency- or effectiveness-
based, and their corresponding target-values. Based on the ﬁndings so far, we provide a deﬁnition of supply chain
risk attitudes as follows. The decision maker’s degree of acceptance with respect to the deterioration of target-values
deﬁnes his attitude towards supply chain risk. Risk-averse supply chain managers only accept a minor deterioration
16

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 18 页

of target values of an efﬁciency- (or effectiveness-) based supply chain goal in exchange for the adherence or increase
of an effectiveness- (or efﬁciency) based supply chain goal. Risk-seeking decision makers, however, accept higher
degrees of value deterioration of a speciﬁc goal in exchange for the adherence or increase of an opposite one. Risk-
neutral supply chain managers prefer neither of the two objective types. If target values of efﬁcient- and effective-
based supply chain goals are too tight, these objectives can be mutually exclusive. For example, a targeted service
level of 100% in addition with a sighted level of zero logistic cost might be impossible.
5. Risk measures
In order to assess and compare different solutions that aim to limit the extent of risk, decision-makers need to
(somehow) quantify risk. Standard deviation, mean-variance approaches, value-at-risk, conditional-value-at-risk or
premiums are risk measures that aim at describing the interaction of uncertainty and the extent of its related harm or
beneﬁt. Owing to the lack of quantitative measures that capture the more complex realities of supply chains, these
measures – developed in ﬁnance and insurance contexts – are applied for supply chain risk, too. Starting from these
concepts, supply chain risk is also measured by the likelihood and the severity of adverse effects or the extent of loss
[45, 56, 97].
In the following, several commonly used supply chain risk measures are introduced and brieﬂy discussed.
Variance or standard deviation are widely used as a measure of supply chain risk, although several authors have
been arguing that they are problematic as measures of risk in general [13, 35, 106]. Both concepts evaluate the
wideness of a distribution and consider not only negative but also positive deviations from expected returns [121].
Consequently, a surplus of the expected is considered as risky as a equal-sized loss. According to Cox the most
common critique in the theoretical decision analysis and ﬁnancial economics literatures are the restrictions under
which the mean-variance analysis is applicable [35], e.g. risk factors have normal or location-scale distributions
and utility functions are quadratic, implying that less money is preferred to more, for some amounts [9, 91]. The
difﬁculties of using probabilities in the light of growing complexity and uncertainty have already been discussed
above. Deviation-based measures, like variance, standard deviation, expected or absolute values of deviation are
applied by [4, 6, 7, 55, 62, 79, 87, 102, 123, 134, 153, 156, 157].
In ﬁnancial engineering and ﬁnancial risk management positive and negative deviations are referred to as upside-
and downside-risk, respectively. In that sense downside-risks reﬂects the risk associated with undesirables outcomes,
i.e. losses. Value-at-risk (V aR) and conditional-value-at-risk (CV aR) are used in portfolio theory as percentile
measures of downside risks. Both concepts describe different parts of a proﬁt or loss distribution and their use is
governed by the objective of the decision maker as well as by the availability and quality of distribution estimates
[121]. V aR is deﬁned as a threshold value associated with a speciﬁed conﬁdence level of outcomes. Let X be a
random variable most often describing a loss and F(X) = Prob{X ≤z} the cumulative distribution function of X.
17

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 19 页

The V aR of X with conﬁdence level α ∈[0, 1) is
V aRα(X) = min{z|FX(z) ≥α}
By deﬁnition V aR is a lower α-percentile of X and therefore does not account for the distribution properties beyond
the conﬁdence interval. The indifference of V aR to extreme parts of the distribution can be both a desirable or
undesirable property. When stable distribution estimates are not available V aR is predominantly used. However,
extreme outcomes impose a particular threat and need to be explained especially if V aR is exceeded. CV aR α(X)
equals the conditional expectation of X subject to X ≥V aRα(X). In other words it describes the average loss
beyond the speciﬁed conﬁdence level. Developed by Rockafellar and Uryasev CV aR attracts much attention due
to its mathematical properties that are especially suitable for optimization problems [118, 121]. Acerbi and Tasche
deﬁned an equivalent of CV aR named expected shortfall [3]. Sarykalin et al. provide a comparative discussion of
both concepts as well as suggestions of when to use which concept [121]. For further insights we refer to their work.
The application of downside risk measures within the context of supply chain problems is very common as can be
deduced from the literature analysis. [86, 111, 123, 125] apply V aR, [111, 123, 124, 125, 137] apply CV aR and
[26, 55, 157] use other downside risk measures.
In actuarial science risk is described by a non-negative random variable, that models a claim size caused by a
policy. Actuaries develop models to quantify and price risks, i.e. they require probability distributions of the risk
regarded as well as preference function to these probability distributions [82]. The price charged by the insurer for
taking the risk is called a premium. The decision to transfer supply chain risk to an insurance has to be investigated
carefully, as it does not necessarily cover the loss of the insured.
Other authors deﬁne approach-speciﬁc concepts like the number of hits [73] or use old-established measures like
the mean-variance related to the proﬁt [85]. Nagurney et al. deﬁne risk functions for each supply chain partner that
depends on the ﬂow related to each partner and on the total ﬂow within the network. These functions are used as
an input for the model. Several authors apply probability as a measure of risk [4, 37, 43, 44, 78]. Azaron et al. for
instance measure the risk associated with a supply chain design problem by the probability of not meeting a certain
cost level or budget [4]. Cui et al. express supply chain risk as the probability that a certain facility serves a certain
customer at a certain level [37]. Some authors do not quantify the degree of risk related to a solution, which is most-
often the case, when supply chain risk is understood as the uncertainty of input parameters [14, 50, 81, 155, 158].
This group is referred to as not further quantiﬁed (NFQ).
Figure 5 summarizes the analysis on risk measures applied in the literature under investigation.
Most approaches concentrate on reducing monetary consequences of uncertain and unexpected developments, see
Section 4.1. Meanwhile they predominantly evaluate the impact of changes of monetary policies (prices) or ﬁscal
policies (taxation) with measures developed for the quantiﬁcation of ﬁnancial risk. However, ﬁnancial risk is taken
care of in ﬁnancial risk management and supply chain risk management should be responsible for monetary losses
18

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 20 页

Downside Risk 32%
[111]
[123]
[125]
[86]
[137] [124]
[26]
[55]
[157]
Probability 9%
[37]
[4]
[78]
[44]
Deviation 34%
[134] [156]
[6]
[79]
[102]
[123]
[55]
[87]
[62]
[7]
[4]
[153]
[157]
NFQ 16%
[155]
[50]
[158]
[81]
[14]
[43]
Other 9%
[100]
[85]
[73]
[159]
Figure 5: Measures applied for quantifying supply chain risk: Downside risk measures like VaR and CVaR and measures of (absolute, expected,
and standard) deviation are among the most applied measures.
within supply chain management. Additionally, we emphasize that objectives of supply chain management have
different dimensions. Effectiveness-driven goals like customer satisfaction or supplier reliability ask for different
measures like efﬁciency-based objectives.
6. Risk-aware Supply Chain Optimization
As supply chain risk management is a discipline that attracts the attention of researchers from different domains,
the existing literature provides various methodological approaches. In addition, the previous discussion has shown
that supply chain risk consists of several relevant aspects. There are literature reviews that analyze the existing work
on some of these core characteristics: Snyder et al. review papers from the operations research community that relate
solely to supply chain disruption, hence that focus on disruptive triggers [133]. Reviews focusing on the affected
supply chain, discuss the design and planning of mitigation alternatives [54, 146]. Afﬁliated work includes topics like
critical infrastructure and network reliability [99, 132].
Others classify and discuss general supply chain risk management approaches more broadly [131, 135, 143, 149]
and derive managerial insights [127, 131, 144, 145].
Tang classiﬁed various quantitative and qualitative approaches upon the supply chain management unit that is
considered to deal with risk (supply, demand, product, or information management) [144]. Within each category the
author further analyzes and differentiates available approaches upon the parameter considered as uncertain (demand,
lead times, costs, yields), problem type (supply network design, supplier relationship, supplier selection process,
19

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 21 页

supplier order allocation, supply contract), management strategy (postponement, process sequencing), or industry,
respectively. Singhal et al. provide a review that classiﬁes literature by research approaches and key issues of supply
chain risk management [131]. They divide analytical risk modeling approaches into modeling type (mathematical,
simulation, and multi-agent) and modeling settings (linear, integer, dynamic, and stochastic problem settings). Ac-
cording to Singhal et al. the latter refers to the nature of the study and scope/domain of the research problem.
The aforementioned surveys give a valuable overview of the supply chain risk management literature reaching
across domains and methodologies. This section provides additional information and insights with the focus set
to mathematical approaches that model supply chain design and planning problems and that explicitly refer to the
consideration of supply chain risk. As we should be interested in how supply chain risk is deﬁned, quantiﬁed, and
modeled today, we omit the aforementioned related work. We analyze the modeling paradigms and techniques that
solve the problems.
6.1. Modeling Approaches
In order to describe mathematical formulations for optimizing supply chain risk problems, this paragraph focuses
on universal categories as well as on aspects tailored for supply chain risk considerations.
Classical categories have been proposed by Beamon among others [12]. He distinguishes between deterministic
analytical, stochastic analytical, economic, and simulation models. Sahebi et al. just recently provided a classiﬁcation
based on Beamon’s and Mula et. al’s approaches [12, 98]. Sahebi et al.’s approach tackles relevant modeling aspects
like the linearity of model formulation, dimensionality of the objective function, analytical model and purpose [122].
This classiﬁcation is more suitable for the analysis of existing literature. Since the purpose of the mathematical
formulation has been analyzed in Section 4.1, this aspect is skipped in the following presentation.
The risk statement is a further relevant aspect of description. Supply chain risk should be either minimized by the
objective function, restricted by speciﬁc constraints or be balanced by its consideration in both statements. Often risk
measures are introduced in the objective function and other risk related parameters are used in constraints.
Considering these aspects, we used the following criteria to classify the models:
• Linear programming, non-linear programming, mixed integer/integer linear programming, mixed integer/ inte-
ger non-linear programming;
• Single and multi-objective functions; and
• Risk considerations within the objective function, within the constraints, or within both.
Table 5 summarizes the various aspects of modeling approaches that classify the reviewed papers.
Table 6 shows the result of this analysis. The majority of the reviewed papers applies linear programmingand more
precisely mixed integer programming approaches. Especially location-allocation type of problems favors the mixed
integer approach [4, 6, 37, 50, 62, 87, 111, 137]. The linear programming approaches considered tactical problems,
20

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 22 页

linearity
linear programming
LP
non linear programming
NLP
mixed integer/integer linear programming
MLP
mixed integer/integer non-linear programming
MNLP
objective function dimensionality
single-objective function
SOF
multi-objective function
MOF
risk statement placement
within objective function
OF
within constraints
CON
within constraints and objective function
OF/CON
Table 5: Categorization of modeling approaches
Ref
Linear
Nonlinear
Objective
Risk statement
LP
MLP
NLP
MNLP
SOF
MOF
OF
CON
OF/CON
[4]
✓
✓
✓
[6]
✓
✓
✓
[7]
✓
✓
✓
[14]
✓
✓
✓
[37]
✓
✓
✓
[43]
✓
✓
✓
[50]
✓
✓
✓
[55]
✓
✓
✓
[62]
✓
✓
✓
[79]
✓
✓
✓
[87]
✓
✓
✓
[102]
✓
✓
✓
[111]
✓
✓
✓
[123]
✓
✓
✓
✓
[124]
✓
✓
✓
✓
[125]
✓
✓
✓
✓
[134]
✓
✓
✓
[137]
✓
✓
✓
[155]
✓
✓
✓
✓
[156]
✓
✓
✓
[157]
✓
✓
✓
✓
[159]
✓
✓
✓
Table 6: Modeling approaches of the reviewed papers
21

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 23 页

Solution Technique
References
Share
General solver, exact solution
[6][7][14][55][111][123][124][125][134][137][156]
46%
General solver, heuristic solution
[14][102][157]
13%
Speciﬁc algorithm, exact solution
[4][37][44][50][62][87]
25%
Speciﬁc algorithm, heuristic solution
[37][43][79][159]
16%
Table 7: Solution techniques of the reviewed papers
like production, logistic or supply chain planning [14, 43, 134, 156, 157] as well as strategic decision models like
supplier selection/portfolio or supply chain design problems [4, 6, 37, 50, 62, 87, 111, 125, 137, 155, 159]. Very
rarely non-linear approaches are chosen [4, 7] Models exclusively considering multi-objective functions are of minor
interest [4, 62, 159], although the need to balance different types of supply chain objectives would motivate multi-
objective approaches. Therefore, the consideration of supply chain risk is stated mainly in both objective function and
constraints.
6.2. Solution Techniques
This section follows the classiﬁcation of solution methods provided by Melo et al. [93]. They deﬁned four
categories that determine different solution techniques. The ﬁrst category General solver, exact solution refers to a
problem’s solution obtained by mathematical programming software. The solution is either optimal or good enough
with respect to a pre-determined acceptable gap speciﬁed by the decision maker. By introducing computational
time restriction an off-the-shelf solver provides solutions of the second category, namely heuristic solution. Speciﬁc
solution algorithms offer exact or heuristic solutions. The former are obtained by special-purpose techniques such
as decomposition methods, column generation, branch-and-cut, and branch-and-bound. The latter are determined by
heuristic-based approaches (Lagrangian relaxation, linear programming based heuristics and meta-heuristics) when
problem sizes are huge. Table 7 summarizes the analysis of solution techniques.
7. Conclusion
An increase in observed supply chain disruptions has raised awareness for supply chain risk management in recent
years. Unfortunately, the understanding of what exactly is meant by supply chain risk, which information should be
monitored, and how risk management and mitigation can be designed in the light of these risks is heterogeneous.
As risk considerations are already deeply embedded in other ﬁelds and partly applied in supply chain management,
we conducted an extensive literature analysis on risk concepts in general and on conceptual as well as mathematical
supply chain risk approaches in particular. Based on the literature review we identiﬁed core characteristics that are
used to deﬁne, quantify and model risk. Adjusted to supply chain risk management these core characteristics can also
deﬁne supply chain risk.
22

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 24 页

The identiﬁcation and discussion of core characteristics allows for a re-deﬁnition of supply chain risk as follows:
Supply chain risk is the potential loss for a supply chain in terms of its target values of efﬁciency and effectiveness
evoked by uncertain developments of supply chain characteristics whose changes were caused by the occurrence of
triggering-events.
However, the real challenge in the ﬁeld of supply chain risk management is still the quantiﬁcation and modeling of
supply chain risk. To this date, supply chain risk management suffers from the lack of a clear and adequate quantitative
measure for supply chain risk that respects the characteristics of modern supply chains. Measures predominantly used
in ﬁnance and insurance are most often used in mathematical approaches for supply chain risk as well. However,
from the aforementioned core characteristics those measures most often address the deviation from efﬁciency-based
objectives. Purely cost- and waste-considering objectives, however, evaluate supply chain’s performance in retrospect.
They miss to assess both operational effectiveness and important strategic achievements like product quality and
customer satisfaction [83]. When it is not possible to fully quantify supply chain risk through risk measures, still
supply chain risk and its related core characteristics need to be represented within supply chain models. Despite
numerous approaches relevant research gaps have been identiﬁed:
• As nowadays supply chains need to fulﬁll efﬁciency- and effectiveness-driven objectives, approaches should
account for balancing these opposite requirements, for example balancing distribution costs and shipment rates,
or overall logistics costs and service level, see Section 4.1.
• More advanced (context-sensitive) approaches especially with respect to the risk attitude of the decision maker
and with respect to the environment of the affected supply chain are needed, see Sections 4.2 and 4.3.
• The impact of time-aspects is evident, their integration into quantitative models, however, challenging, see
Section 4.2.
Besides categorizing available approaches and identifying research gaps, the underlying review clariﬁed the meaning
and importance of notions commonly used within the (supply chain) risk management literature.
8. Acknowledgment
Some of the authors have received ﬁnancial support from BASF SE (Germany) within a research program.
References
[1] Iso 14971:2007 – medical devices – application of risk management to medical devices, Accessed July, 2014.
[2] Kenneth J. Aarrow. Risk perception in psychology and economics. Economic Inquiry, 20:1–9, 1982.
[3] C. Acerbi and D. Tasche. On the coherence of expected shortfall. Journal of Banking and Finance, 26:14871503, 2002.
[4] A. Azaron, K. N. Brown, S. A. Tarim, and M. Modarres. A multi-objective stochastic programming approach for supply chain design
considering risk. International Journal of Production Economics, 116(1):129–138, 2008.
23

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 25 页

[5] V´ıctor A. Ba˜nuls and Murray Turoff. Scenario construction via Delphi and cross-impact analysis. Technological Forecasting and Social
Change, 78(9):1579–1602, 2011.
[6] Reza Babazadeh and Jafar Razmi. A robust stochastic programming approach for agile and responsive logistics under operational and
disruption risks. International Journal of Logistics Systems and Management, 13(4):458–482, 2012.
[7] Atefeh Baghalian, Shabnam Rezapour, and Reza Zanjirani Farahani. Robust supply chain network design with service level against disrup-
tions and demand uncertainties: A real-life case. European Journal of Operational Research, 227(1):199–215, 2013.
[8] Paul Barnes and Richard Oloruntoba. Assurance of security in maritime supply chains: conceptual issues of vulnerability and crisis man-
agement. Journal of International Management, 11:519–540, 2005.
[9] D.P. Baron. On the utility-theoretic foundation of mean-variance analysis. Journal of Finance, 32(5):1683–1697, 1977.
[10] AP Barroso, VH Machado, and V Cruz Machado. Identifying vulnerabilities in the supply chain. In Industrial Engineering and Engineering
Management, 2009. IEEM 2009. IEEE International Conference on, pages 1444–1448. IEEE, 2009.
[11] Basel Committee on Banking Supervision. International convergence of capital measurement and capital standards. Technical report, Bank
for international settlements, 2004. ISBN: 92-9131-669-5.
[12] Benita M. Beamon. Supply chain design and analysis: Models and methods. International Journal of Production Economics, 55(3):281–294,
1998.
[13] D. Bell. Measuring risk and return of portfolios. In Wise Choices. HBS Publishing, 1996.
[14] Aharon Ben-Tal, Byung Do Chung, Supreet Reddy Mandala, and Tao Yao. Robust optimization for emergency logistics planning: Risk
mitigation in humanitarian relief supply chains. Transportation research part B: methodological, 45(8):1177–1189, 2011.
[15] Katja Berdica. An introduction to road vulnerability: what has been done, is done and should be done. Transport Policy, 9(2):117–127,
2002.
[16] Peter L. Bernstein. Against the Gods: The Remarkable Story of Risk. John Wiley, New York, 1998.
[17] J¨orn Birkmann. Measuring Vulnerability To Natural Hazards, chapter Measuring vulnerability to promote disaster-resilient societies: Con-
ceptual frameworks and deﬁnitions, pages 9–53. TERI, New Delhi, 2006.
[18] Arjen Boin and Allan McConnell.
Preparing for critical infrastructure breakdowns: the limits of crisis management and the need for
resilience. Journal of Contingencies and Crisis Management, 15(1):50–59, 2007.
[19] B. Borgstr¨om.
Exploring efﬁciency and effectiveness in the supply chain: a conceptual analysis.
In Proceedings from the 21st IMP
Conference, Rotterdam, Netherlands, 2005.
[20] Glynis Marie Breakwell. The psychology of risk. Cambridge University Press Cambridge, 2007.
[21] John Y Campbell and Luis M Viceira. Strategic asset allocation: portfolio choice for long-term investors. Oxford University Press, 2002.
[22] Omar Cardona. The need for rethinking the concepts of vulnerability and risk from a holistic perspective: A necessary review and criticism
for effective risk management. In G. Bankoff, G. Frerk, and D. Hillhorst, editors, Mapping Vulnerability: Disasters, Development and
People, pages 37–51. Earthscan Publications, London, UK, 2004.
[23] H. Carvalho and V. Cruz Machado. Integrating lean, agile, resilience and green paradigms in supply chain management. In Pengzhong Li,
editor, Supply Chain Management, pages 66–76. InTech, 2011.
[24] J. L Cavinato. Supply chain logistics risks. International Journal of Physical Distribution & Logistics Management, 34(5):383–387, 2004.
[25] Paul Chapman, Martin Christopher, Uta J¨uttner, Helen Peck, and Richard Wilding. Identifying and managing supply-chain vulnerability.
Logistics & Transport Focus, 4(4):59–64, 2002.
[26] F. Y. Chen and C. A. Yano. Improving supply chain performance and managing risk under weather-related demand uncertainty. Management
Science, 56(8):1380–1397, 2010.
[27] Thomas J. Chermack. Improving decision-making with scenario planning. Futures, 36(3):295–309, 2004.
[28] S. Chopra and M. M.S Sodhi. Managing risk to avoid supply-chain breakdown. MIT Sloan Management Review, 46(1):53–61, 2004.
[29] M. Christopher and H. Lee.
Supply chain conﬁdence: The key to effective supply chains through improved visibility and reliability.
Technical report, Cranﬁeld University and Stanford University, 2001.
24

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 26 页

[30] Martin Christopher and Helen Peck. Building the resilient supply chain. International Journal of Logistics Management, 15(2):1–13, 2004.
[31] L. Coleman. Frequency of man-made disasters in the 20th century. Journal of Contingencies and Crisis Management, 15:1–13, 2006.
[32] Tina Comes, Michael Hiete, Niek Wijngaards, and Frank Schultmann. Decision Maps: A framework for multi-criteria decision support
under severe uncertainty. Decision Support Systems, 52(1):108–118, 2011.
[33] Louise K. Comfort. Crisis management in hindsight: Cognition, communication, coordination, and control. Public Administration Review,
67:189–197, 2007.
[34] D.F. Cox. Risk-taking and information-handling in consumer behavior. Boston: Harvard University Press, 1967.
[35] L.A. Cox. Why risk is not variance: An expository note. Risk Analysis, 28(4):925–928, 2008.
[36] C. W. Craighead, J. Blackhurst, M. J. Rungtusanatham, and R. B. Handﬁeld. The severity of supply chain disruptions: Design characteristics
and mitigation capabilities. Decision Sciences, 38:131–156, 2007.
[37] Tingting Cui, Yanfeng Ouyang, and Zuo-Jun Max Shen. Reliable facility location design under the risk of disruptions. Operations Research,
58(4-part-1):998–1011, 2010.
[38] Amos Tversky Daniel Kahneman. Prospect theory: an analysis of decision under risk. Econometrica, 47(2):263–292, 1979.
[39] B. de Finetti. Il problema dei pieni. Giorn. Ist. Ital. Atturi, 11:1–88, 1940.
[40] DNV - Det Norske Veritas. Risk - a word from ancient greece, 2012.
[41] Scott C Ellis, Raymond M Henry, and Jeff Shockley. Buyer perceptions of supply disruption risk: a behavioral view and empirical assess-
ment. Journal of Operations Management, 28(1):34–46, 2010.
[42] Mauro Falasca, Christopher W Zobel, and Deborah Cook. A decision support framework to assess supply chain resilience. In F. Friedrich
and B. Van de Walle, editors, 5th ISCRAM Conference, pages 596–605, Washington, DC, USA, 2008.
[43] J. Fang, L. Zhao, J. C. Fransoo, and T. Van Woensel. Sourcing strategies in supply risk management: An approximate dynamic programming
approach. Computers and Operations Research, 40(5):1371–1382, 2013.
[44] Awi Federgruen and Nan Yang. Optimal supply diversiﬁcation under general supply risks. Operations Research, 57(6):1451–1468, 2009.
[45] Peter C. Fishburn. Foundations of Risk Measurement. I. Risk As Probable Loss. Management Science, 30(4):396–406, 1984.
[46] Simon French. Cyneﬁn, Statistics and Decision Analysis. Journal of the Operational Research Society, online:accepted, 2012.
[47] M. Frosdick. The techniques of risk management are insufﬁcient in themselves. Disaster prevention and Management, 6(3):165–177, 1997.
[48] Boon Ping Gan, Li Liu, Sanjay Jain, Stephen J. Turner, Wentong Cai, and Wen-Jing Hsu. Manufacturing supply chain management:
distributed supply chain simulation across enterprise boundaries. In Proceedings of the 32nd conference on Winter simulation, pages 1245–
1251, San Diego, CA, USA, 2000. Society for Computer Simulation International.
[49] T.S. Glickmann and S.C. White. Security, visibility and resilience: The keys to mitigating supply chain vulnerabilities. International Journal
of Logistics Systems and Management, 2(2):10–119, 2006.
[50] M. Goh, J. Y. S. Lim, and F. Meng. A stochastic model for risk management in global supply chain networks. European Journal of
Operational Research, 182(1):164–173, 2007.
[51] Christian Gollier. The economics of risk and time. MIT press, 2004.
[52] U. G¨otze and B. Mikus. Der Prozess des Risikomanagements in Supply Chains. In R. Vahrenkamp and C. Siepermann, editors, Risikoman-
agement in Supply Chains, pages 29–58. Erich Schmidt Verlag GmbH & Co. Berlin, 2007.
[53] S.M. Grundy, R. Pasternak, P. Greenland, S. Smith, and V. Fuster. Assessment of cardiovascular risk by use of multiple-risk-factor as-
sessment equations: A statement for healthcare professionals from the american heart association and the american college of cardiology.
Journal of the American College of Cardiology, 34(4):1348–1359, 1999.
[54] Haresh Gurnani, Anuj Mehrotra, and Saibal Ray, editors. Supply Chain Disruptions: Theory and Practice of Managing Risk. Springer,
2011.
[55] G.J. Hahn and H. Kuhn. Value-based performance and risk management in supply chains: A robust optimization approach. International
Journal of Production Economics, 139(1):135–144, 2012.
[56] Yacov Y. Haimes, Stan Kaplan, and James H. Lambert. Risk Filtering, Ranking, and Management Framework Using Hierarchical Holo-
25

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 27 页

graphic Modeling. Risk Analysis, 22(2):383–398, 2002.
[57] Raimo P. H¨am¨al¨ainen, Mats R.K. Lindstedt, and Kari Sinkko. Multiattribute risk analysis in nuclear emergency management. Risk Analysis,
20(4):455–468, 2000.
[58] Dirk Helbing, Hendrik Ammoser, and Christian K¨uhnert. Disasters as Extreme Events and the Importance of Network Interactions for
Disaster Response Management. In Sergio Albeverio, Volker Jentsch, and Holger Kantz, editors, Extreme Events in Nature and Society, The
Frontiers Collection, pages 319–348. Springer Berlin Heidelberg, 2006.
[59] Dirk Helbing and Stefan L¨ammer. Managing Complexity: An Introduction. In D. Helbing, editor, Managing Complexity: Insights, Concepts,
Applications, volume 32 of Understanding Complex Systems, pages 1–16. Springer Berlin, Heidelberg, 2008.
[60] Alan Hodges. Emergency risk management. Risk Management, 2(4):7–18, 2000.
[61] H˚akan H˚akansson and Frans Prenkert. Exploring the exchange concept in marketing. In Rethinking Marketing - developing a new under-
standing of markets. H˚akan H˚akansson & Alexandra Walnuszewski, 2004.
[62] Edward Huang and Marc Goetschalckx. Strategic robust supply chain design based on the pareto-optimal tradeoff between efﬁciency and
risk. European Journal of Operational Research, 237(2):508 – 518, 2014.
[63] John Hull. Options, futures, and other derivatives. Pearson, Prentice Hall, Upper Saddle River, NJ, 6. ed. edition, 2006.
[64] John Hull. Risk Management and Financial Institutions. John Wiley & Sons, 2012.
[65] Erik Jenelius and Lars-Gran Mattsson. Road network vulnerability analysis of area-covering disruptions: A grid-based approach with case
study. Transportation Research Part A: Policy and Practice, 46(5):746 – 760, 2012.
[66] U. J¨uttner and S. Maklan. Supply chain resilience in the global ﬁnancial crisis: An empirical study. Supply Chain Management, 16(4):246–
259, 2011.
[67] U. J¨uttner, H. Peck, and M. Christopher. Supply chain risk management: outlining an agenda for future research. International Journal of
Logistics Research and Applications, 6(4):197–210, 2003.
[68] Uta J¨uttner. Supply chain risk management: Understanding the business requirements from a practitioner perspective. The International
Journal of Logistics Management, 16(1):120–141, 2005.
[69] Peter Kaj¨uter. Instrumente zum Risikomanagement in der Supply Chain. In Supply Chain Controlling in Theorie und Praxis. Wolfgang
Stlzle und Andreas Otto, 2003.
[70] Peter Kaj¨uter.
Risikomanagement in der Supply Chain: ¨Okonomische, regulatorische und konzeptionelle Grundlagen.
In Richard
Vahrenkamp and Christoph Siepermann, editors, Risikomanagement in Supply Chains, pages 13–27. Erich Schmidt Verlag GmbH & Co.
Berlin, 2007.
[71] W. Kersten, T. Held, C.M. Meyer, and P. Hohrath. Komplexit¨ats- und Risikomanagement als Methodenbausteine des Supply Chain Man-
agements. In Management am Puls der Zeit – Strategien, Konzepte und Methoden. I. Hausladen & C. Mauch, 2007.
[72] Wolfgang Kersten, Mareike Bger, Philipp Hohrath, and Hagen Sp¨ath. Supply chain risk management: Development of a theoretical and
empirical framework.
In Wolfgang Kersten and Thomas Blecker, editors, Managing Risks in Supply Chains - How to Build Reliable
Collaboration in Logistics, pages 3–18. Erich Schmidt Verlag GmbH & Co. Berlin, 2006.
[73] W. Klibi and A. Martel. Scenario-based supply chain network risk modeling. European Journal of Operational Research, 223:644–658,
2012.
[74] Andreas Klinke and Ortwin Renn. A New Approach to Risk Evaluation and Management: Risk-Based, Precaution-Based, and Discourse-
Based Strategies. Risk Analysis, 22(6):1071–1094, 2002.
[75] F. Knight. Risk, Uncertainty, and Proﬁts. Hart, Schaffner, and Marx, 1921.
[76] George L. Kovacs and Paolo Paganelli. A planning and management infrastructure for large, complex, distributed projects–beyond ERP and
SCM. Computers in Industry, 51(2):165–183, 2003.
[77] AM Kuhn and BJ Youngberg. The need for risk management to evolve to assure a culture of safety. Quality and Safety in Health Care,
11(2):158–162, 2002.
[78] T. Kull and D. Closs. The risk of second-tier supplier failures in serial supply chains: Implications for order policies and distributor
26

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 28 页

autonomy. European Journal of Operational Research, 186(3):1158–1174, 2008.
[79] Sri Krishna Kumar, MK Tiwari, and Radu F Babiceanu.
Minimisation of supply chain cost with embedded risk using computational
intelligence approaches. International Journal of Production Research, 48(13):3717–3739, 2010.
[80] P. Kupsch. Risikomanagement. In Handbuch Unternemehensfhrung. Konzepte - Instrumente - Schnittstellen. Corsten, H., Rei, M., 1995.
[81] Guoming Lai, Laurens G Debo, and Katia Sycara. Sharing inventory risk in supply chain: The implication of ﬁnancial constraint. Omega,
37(4):811–825, 2009.
[82] Z. Landsman and M. Sherris. Risk measures and insurance premium principles. Insurance: Mathematics and Economics, 29(1):103–115,
2001.
[83] Larry Lapide. What about measuring supply chain performance?
Achieving Supply Chain Excellence Through Technology, 2:287–297,
2000.
[84] Robert J. Lempert and David G. Groves. Identifying and evaluating robust adaptive policy responses to climate change for water management
agencies in the american west. Technological Forecasting and Social Change, 77(6):960–974, 2010.
[85] Zugang Liu and Anna Nagurney. Supply chain outsourcing under exchange rate risk and competition. Omega, 39(5):539–549, 2011.
[86] Archie Lockamy III and Kevin McCormack. Analysing risks in supply networks to facilitate outsourcing decisions. International Journal
of Production Research, 48(2):593–611, 2010.
[87] H. . Mak and Z. . Shen. Risk diversiﬁcation and risk pooling in supply chain design. IIE Transactions (Institute of Industrial Engineers),
44(8):603–621, 2012.
[88] Ila Manuj and John T Mentzer. Global supply chain risk management strategies. International Journal of Physical Distribution & Logistics
Management, 38(3):192–223, 2008.
[89] Siambabala Bernard Manyena. The concept of resilience revisited. Disasters, 30(4):434–450, 2006.
[90] J. G March and Z. Shapira. Managerial perspectives on risk and risk taking. Management science, 33(11):1404–1418, 1987.
[91] Harry Markowitz. Portfolio selection. The Journal of Finance, 7(1):77–91, 1952.
[92] Alexander J. McNeil, R¨udiger Frey, and Paul Embrechts. Quantitative Risk Management: Concepts, Techniques and Tools. Princeton
University Press, 2005.
[93] M.T. Melo, S. Nickel, and F. Saldanha-da-Gama. Facility location and supply chain management - a review. European Journal of Opera-
tional Research, 196:401–412, 2009.
[94] Merriam-Webster, 2013.
[95] Mirjam Merz, Michael Hiete, Tina Comes, and Frank Schultmann. A composite indicator model to assess natural disaster risks in industry
on a spatial level. Journal of Risk Research, 16(9):1077–1099, 2013.
[96] K. E. Kristian M¨oller and Pekka T¨orr¨onen. Business suppliers’ value creation potential: A capability-based analysis. Industrial Marketing
Management, 32(2):109–118, 2003.
[97] Millet Granger Morgan and Max Henrion. Uncertainty: A Guide to Dealing with Uncertainty in Quantitative Risk and Policy Analysis.
Cambridge University Press, Cambridge, 1990.
[98] Josefa Mula, David Peidro, Manuel D´ıaz-Madro˜nero, and Eduardo Vicens. Mathematical programming models for supply chain production
and transport planning. European Journal of Operational Research, 204(3):377–390, 2010.
[99] A. T. Murray and T. H. Grubesic, editors. Reliability and Vulnerability in Critical Infrastructure: A Quantitative Geographic Perspective.
Springer, 2006.
[100] Anna Nagurney, Jose Cruz, June Dong, and Ding Zhang. Supply chain networks, electronic commerce, and supply side and demand side
risk. European Journal of Operational Research, 164(1):120–142, 2005.
[101] A. Norrman and J. Jansson. Ericsson’s proactive supply chain risk management approach after a serious sub-supplier accident. International
Journal of Physical Distribution & Logistics Management, 35(5):434–453, 2004.
[102] F. Oliveira, V. Gupta, S. Hamacher, and I. E. Grossmann. A lagrangean decomposition approach for oil supply chain investment planning
under uncertainty with risk considerations. Computers and Chemical Engineering, 50:184–195, 2013.
27

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 29 页

[103] S. H. Owen and M. S. Daskin. Strategic facility location: A review. European Journal of Operational Research, 111:423–447, 1998.
[104] H. Peck. Drivers of supply chain vulnerability: an integrated framework.
International Journal of Physical Distribution & Logistics
Management, 35(4):210–232, 2005.
[105] H. Peck. Reconciling supply chain vulnerability, risk and supply chain management. International Journal of Logistics Research and
Applications, 9(2):127–142, 2006.
[106] C.
S. Pedersen
and
S. E. Satchell.
Choosing
the
right
risk
measure:
A
survey.
Technical
report,
Available
at
http://citeseer.ist.psu.edu/52(0923).html, 1998.
[107] M. Peng, Y. Peng, and H. Chen. Post-seismic supply chain risk management: A system dynamics disruption analysis approach for inventory
and logistics planning. Computers and Operations Research, 42:14–24, 2014.
[108] William J. Petak. Emergency management: A challenge for public administration. Public Administration Review, 45:3–7, 1985.
[109] Timothy J. Pettit, Joseph Fiksel, and Keely L. Croxton. Ensuring supply chain resilience: Development of a conceptual framework. Journal
of Business Logistics, 31(1):1 – 21, 2010.
[110] S.Y. Ponomarov and M. C. Holcomb. Understanding the concept of supply chain resilience. International Journal of Logistics Management,
20(1):124–143, 2009.
[111] C. A. Poojari, C. Lucas, and G. Mitra. Robust solutions and risk measures for a supply chain planning problem under uncertainty. Journal
of the Operational Research Society, 59(1):2–12, 2008.
[112] Joseph E. Quansah, Bernard Engel, and Gilbert L. Rochon. Early warning systems: A review. Journal of Terrestrial Observation, 2(2):24–
44, 2010.
[113] Andrea Renda. Protecting critical infrastructure in the EU. CEPS task force report, Centre for European Studies, Brussels, 2010.
[114] J.B. Rice and F. Caniato. Building a secure and resilient supply network. Supply Chain Management Review, 7(5):22–30, 2003.
[115] R Glenn Richey Jr. The supply chain crisis and disaster pyramid: a theoretical framework for understanding preparedness and recovery.
International Journal of Physical Distribution & Logistics Management, 39(7):619–628, 2009.
[116] Risk Response Network. New models for addressing supply chain and transport risk. Technical report, The World Economic Forum, 2011.
[117] Risk Response Network. Building resilience in supply chains. Technical report, The World Economic Forum, 2013.
[118] R Tyrrell Rockafellar and Stanislav Uryasev. Optimization of conditional value-at-risk. Journal of risk, 2:21–42, 2000.
[119] J. Rosenhead, M. Elton, and S. Gupta. Robustness and optimality as criteria for strategic decisions. Operational Research Quaterly,
23(4):413–430, 1972.
[120] Ivan Ross. Perceived risk and consumer behavior: a critical review. Advances in Consumer Research, 2(1):1–20, 1975.
[121] Sarykalin S., Serraino G., and Uryasev S. Value-at-risk vs. conditional value-at-risk in risk management and optimization. In Tutorials in
Operations Research, page 27094. INFORMS, 2008.
[122] Hadi Sahebi, Stefan Nickel, and Jalal Ashayeri. Strategic and tactical mathematical programming models within the crude oil supply chain
context. Computers & Chemical Engineering, 68:56–77, 2014.
[123] T. Sawik. Integrated selection of suppliers and scheduling of customer orders in the presence of supply chain disruption risks. International
Journal of Production Research, 51(23-24):7006–7022, 2013.
[124] T. Sawik. Optimization of cost and service level in the presence of supply chain disruption risks: Single vs. multiple sourcing. Computers
and Operations Research, 51:11–20, 2014.
[125] Tadeusz Sawik. Selection of supply portfolio under disruption risks. Omega, 39(2):194 – 208, 2011.
[126] A. J. Schmitt and M. Singh. A quantitative analysis of disruption risk in a multi-echelon supply chain. International Journal of Production
Economics, 139(1):22–32, 2012.
[127] Y. Shefﬁ. The Resilient Enterprise. The MIT Press, 2007.
[128] Y. Shefﬁand B. Rice. A supply chain view of the resilient enterprise. Technical report, MIT Sloan Management review, 2005.
[129] D. Simchi-Levi, P. Kaminsky, and E. Simchi-Levi. Designing and Managing the Supply Chain. McGraw-Hill/Irwin, 2008.
[130] David Simchi-Levi. Operations rules. MIT Press, 2010.
28

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 30 页

[131] Piyush Singhal, Gopal Agarwal, and Murali Lal Mittal. Supply chain risk management: review, classiﬁcation and future research directions.
Int. Journal of Business Science and Applied Management, 6(3):15–42, 2011.
[132] J. C. Smith. Basic Interdiction Models. Wiley Encyclopedia of Operations Research and Management Science, 2010.
[133] Lawrence V Snyder, Zumbul Atan, Peng Peng, Ying Rong, Amanda J Schmitt, and Burcu Sinsoysal. Or/ms models for supply chain
disruptions: A review. Available at SSRN 1689882, 2012.
[134] M. S. Sodhi. Managing demand risk in tactical supply chain planning for a global consumer electronics company. Production and Operations
Management, 14(1):69–79, 2005.
[135] ManMohan S. Sodhi, Byung-Gak Son, and Christopher Tang. Researchers perspective on supply chain risk management. Production and
Operations Management, 21(1):1–13, 20012.
[136] ManMohan S. Sodhi and Christopher Tang. Managing supply chain disruptions via time-based risk management. In Teresa Wu and Jennifer
Blackhurst, editors, Managing Supply Chain Risk and Vulnerability – Tools and Methods for Supply Chain Decision Makers. Springer, 2009.
[137] H. Soleimani and K. Govindan. Reverse logistics network design and planning utilizing conditional value at risk. European Journal of
Operational Research, 2014. Article in Press.
[138] J. Stock and S. Boyer. Developing a consensus deﬁnition of supply chain management: A qualitative study. International Journal of Physical
Distribution & Logistics Management, 39(8):690–711, 2009.
[139] Supply Chain Digest. The greatest supply chain disasters of all time 2009. Technical report, Supply Chain Digest, 2009.
[140] G. Svensson. A conceptual framework for the analysis of vulnerability in supply chains. International Journal of Physical Distribution &
Logistics Management, 30(9):731–750, 2000.
[141] G. Svensson. Dyadic vulnerability in companies’ inbound and outbound logistics ﬂows. Journal of Logistics: Research and Applications,
5(1):81–113, 2002.
[142] G. Svensson. Vulnerability in business relationships: the gap between dependence and trust. Journal of Business & Industrial Marketing,
19(7):469–483, 2004.
[143] Ou Tang and S Nurmaya Musa. Identifying risk issues and research advancements in supply chain risk management. International Journal
of Production Economics, 133(1):25–34, 2011.
[144] S. Tang. Perspectives in supply chain risk management. International Journal of Production Economics, 103:451–488, 2006.
[145] S. Tang. Robust strategies for mitigating supply chain disruptions. International Journal of Logistics, 9:33–45, 2006.
[146] Brian Tomlin. On the value of mitigation and contingency strategies for managing supply chain disruption risks. Management Science,
52(5):639–657, 2006.
[147] United Nations Inter-Agency Secretariat of the International Strategy for Disaster Reduction (UN/ISDR). Living with risk: a global review
of disaster reduction initiatives, volume II. United Nations publication, New York and Geneva, 2004.
[148] Bartel Van de Walle and Murray Turoff. Decision support for emergency situations. Information Systems and E-Business Management,
6(3):295–316, 2008.
[149] I. Vanany, S. Zailani, and N. Pujawan. Supply chain risk management: Literature review and future research. International Journal of
Information Systems and Supply Chain Management, 2(1):16–33, 2009.
[150] S. Wagner and C. Bode. An empirical investigation into supply chain vulnerability.
Journal of Purchasing and Supply Management,
12(6):301–312, 2006.
[151] S. M. Wagner and C. Bode. An empirical examination of supply chain performance along several dimensions of risk. Journal of Business
Logistics, 29:307–325, 2008.
[152] Stephan M. Wagner and Christoph Bode. Dominant risks and risk management practices in supply chains. In George A. Zsidisin and Bob
Ritchie, editors, Supply Chain Risk, volume 124 of International Series in Operations Research & Management Science, pages 271–290.
Springer, 2009.
[153] T. Wakolbinger and J. M. Cruz. Supply chain disruption risk management through strategic information acquisition and sharing and risk-
sharing contracts. International Journal of Production Research, 49(13):4063–4084, 2011.
29

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 31 页

[154] D. Waters. Supply Chain Risk Management. Kogan Page Limited, 2007.
[155] D. Wu and D. L. Olson. Supply chain risk, simulation, and vendor selection. International Journal of Production Economics, 114(2):646–
655, 2008.
[156] Y. Wu. Robust optimization applied to uncertain production loading problems with import quota limits under the global supply chain
management environment. International Journal of Production Research, 44(5):849–882, 2006.
[157] Fengqi You, John M Wassick, and Ignacio E Grossmann. Risk management for a global supply chain planning under uncertainty: models
and algorithms. AIChE Journal, 55(4):931–946, 2009.
[158] H. Yu, A. Z. Zeng, and L. Zhao. Single or dual sourcing: decision-making in the presence of supply chain disruption risks. Omega,
37(4):788–800, 2009.
[159] M. . Yu and M. Goh. A multi-objective approach to supply chain visibility and risk. European Journal of Operational Research, 233(1):125–
130, 2014.
[160] Arne Ziegenbein. Supply Chain Risiken: Identiﬁkation, Bewertung und Steuerung, volume 15. vdf Hochschulverlag AG, 2007.
[161] H.-J. Zimmermann. An application-oriented view of modeling uncertainty. European Journal of Operational Research, 122:190–198, 2000.
[162] George A Zsidisin. A grounded deﬁnition of supply risk. Journal of Purchasing and Supply Management, 9(5):217–224, 2003.
30

*（本页包含 1 张图片，请参阅原PDF）*

---
