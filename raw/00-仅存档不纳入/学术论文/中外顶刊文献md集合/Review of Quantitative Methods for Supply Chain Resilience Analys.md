# Review of Quantitative Methods for Supply Chain Resilience Analys

> **源文件**: Review of Quantitative Methods for Supply Chain Resilience Analys.pdf
> **页数**: 48

---

## 第 1 页

The University of Southern Mississippi
The University of Southern Mississippi
The Aquila Digital Community
The Aquila Digital Community
Faculty Publications
5-1-2019
Review of Quantitative Methods for Supply Chain Resilience
Review of Quantitative Methods for Supply Chain Resilience
Analysis
Analysis
Seyedmohsen Hosseini
University of Southern Mississippi, mohsen.hosseini@usm.edu
Dmitry Ivanov
Berlin School of Economics and Law, divanov@hwr-berlin.de
Alexandre Dolgui
IMT Atlantique, alexandre.dolgui@imt-atlantique.fr
Follow this and additional works at: https://aquila.usm.edu/fac_pubs
Part of the Operations and Supply Chain Management Commons
Recommended Citation
Recommended Citation
Hosseini, S., Ivanov, D., Dolgui, A. (2019). Review of Quantitative Methods for Supply Chain Resilience
Analysis. Transportation Research E: Logistics and Transportation Review, 125, 285-307.
Available at: https://aquila.usm.edu/fac_pubs/16043
This Article is brought to you for free and open access by The Aquila Digital Community. It has been accepted for
inclusion in Faculty Publications by an authorized administrator of The Aquila Digital Community. For more
information, please contact aquilastaff@usm.edu.

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 2 页

Review of quantitative methods for supply chain resilience analysis
Seyedmohsen Hosseini
Industrial Engineering Technology, University of Southern Mississippi,
730 East Beach Boulevard, Long Beach, MS, USA
Email: mohsen.hosseini@usm.edu
Dmitry Ivanov
Supply Chain Management, Berlin School of Economics and Law, Berlin, Germany
Email: divanov@hwr-berlin.de
Alexandre Dolgui
Automation, Production and Computer Sciences Dept.
IMT Atlantique LS2N - CNRS UMR 6004 La Chantrerie, France
E-Mail: alexandre.dolgui@imt-atlantique.fr
Abstract
Supply chain resilience (SCR) manifests when the network is capable to withstand, adapt, and recover from
disruptions to meet customer demand and ensure performance. This paper conceptualizes and comprehen-
sively presents a systematic review of the recent literature on quantitative modeling the SCR while distinc-
tively pertaining it to the original concept of resilience capacity. Decision-makers and researchers can ben-
efit from our survey since it introduces a structured analysis and recommendations as to which quantitative
methods can be used at different levels of capacity resilience. Finally, the gaps and limitations of existing
SCR literature are identified and future research opportunities are suggested.
Keywords: Supply chain resilience, Disruption risk, Resilience supplier, Supply disruptions, Review, Re-
silient supply chain, Capacity resilience, Ripple effect, Digital supply chain
 Corresponding author

---

## 第 3 页

1. Introduction
In today’s global and increasingly dynamic and turbulent environments, supply chains (SC) are
confronted with numerous events that threaten to disrupt SC operational activities and jeopardize
efficient and effective performance. Disruption risks are events caused by natural catastrophes,
such as hurricanes, earthquakes, or floods, or by man-made threats, such as terrorist attacks or
labor strikes. Disruption risks typically refer to low likelihood, but high impact events, which un-
predictably vary in type, scale and nature, are intermittent and irregular to be identified, estimated
and forecasted well, and may have short or long term negative effects (Ho et al. 2015, Torabi et
al. 2015, Dolgui et al. 2018, He et al. 2018).
For example, as a result of the tsunami and earthquake that struck Japan in 2011, Toyota’s parts
suppliers were unable to deliver parts at the expected volume and time. This forced Toyota to halt
production for several days. Similarly, General Motors was forced to stop production because of
a shortage of raw materials from their Japanese suppliers (Huffington Post 2015). Nissan suffered
significant setbacks: the company had a high level of dependency on raw materials from suppliers
who were located in the tsunami and earthquake zone and supplied 12% of Nissan’s engines (BBC
News 2011). Nissan had to temporarily shut down production at its Sunderland UK plant.
The Japanese tsunami and earthquake also impacted the aerospace industries. Boeing Company
retained collaboration with Japanese manufacturers and suppliers because of the punctuality of
their deliveries and their quality of production. Five Japanese companies, including Mitsubishi
Heavy Industries Ltd., produce structural parts comprising 21% of the 777 wide body jet and 35%
of the 787 jet aircraft, making Japan the largest supplier of the 777 and 787, after the U.S. (Bloom-
berg 2014). The Japanese tsunami shook aerospace SCs. Three first-tier aerospace suppliers,
Mitsubishi Heavy Industries, Kawasaki Heavy Industries, and Fuji Heavy Industries, were located
in a disruption-prone zone.  Shares of those three companies dropped a minimum of 1.2% and a
maximum of 6%, following the disaster (Reuters 2011).
The examples given provide evidence that SC systems must be designed so that they can withstand
disruptions (low vulnerability) and recover from disruptions quickly and at a minimal cost (high
recoverability). In other words, the question of SC resilience (SCR) arises when designing global
supply networks. SCR manifests when the network is capable to withstand, adapt, and recover
from disruptions to meet customer demand and ensure performance.

---

## 第 4 页

In the last decade, SCR has been transitioning from an emerging topic to a rapidly growing re-
search area: model taxonomies need to be developed, and different types of operational research
techniques and generic applications and trends classified. Though there are very few literature
reviews on SCR, existing ones are conceptually and empirically-oriented. Notwithstanding the
growing number of publications on SCR, there are few studies that focus on quantifying attributes
of resilience in SCs. Existing surveys tend to focus on the qualitative (conceptual) aspects of SCR.
Fiksel (2003) provided insights on how firms, corporations, and SC companies can handle disrup-
tive events, such as loss of a supplier, labor strikes, or transportation disasters, in order to maintain
acceptable competitive advantages. Tukamuhabwa et al. (2015) presented a survey paper that de-
fines and reviews conceptual factors that could improve the resilience of SCs. Kamalahmadi and
Mellat-Parast (2016) analyzed the definitions and drivers of enterprise resilience, as well as the
principles of SCR. Several commonalities can be observed across existing surveys. The authors
aim to identify and analyze the factors that contribute to SCR from a qualitative standpoint. The
majority of factors discussed in these surveys are qualitative or semi-qualitative. For example,
Japanese automotive companies tried to collaborate with auto part suppliers being geographically
dispersed to reduce the risk impact likelihood of their SCs. Auto manufacturing companies recon-
sidered their backup and emergency inventory. Geographic separation of suppliers and holding
excess backup and emergency inventory are considered as a two resilience enhancement features
for auto manufacturers. When reviewing disruptive examples in the SCs and suggested mitigation
and recovery policies in literature, the analysis highlights a greater geographic distribution of pro-
duction facilities, protection of manufacturing sites as well as operational redundancies and flexi-
bilities in capacity and inventory. Left ignored, however, was the deciphering of the SCR factors
according to different levels of disruption severity – an important SCR dimension which our study
is pertained to.
The importance of quantitative methods to studying SC disruption risk has been highlighted in
surveys by Fahimnia et al. (2015a), Ho et al. (2015) and Snyder et al. (2016). Riberio and Babosa-
Povoa’s (2018) survey highlighted the importance of quantitative analysis of SCR. The reviews of
quantitative methods by Ivanov et al. (2017b) and Dolgui et al. (2018) direct attention to specific
aspects of SCR, i.e., recovery stages, and the ripple effect in the SC, respectively. Ivanov and
Dolgui (2018) developed a classification scheme for analyzing SC disruption risk literature. None
of these studies, though, presented a systematic review of the recent literature on quantitative SCR

---

## 第 5 页

modeling considering in a structured way different levels of SCR – a distinctive and significant
contribution made by our study relying on the original concept of resilience capacity. In addition,
the existing surveys do not systematically specify how the qualitative SCR factors can be opera-
tionalized in the quantitative models. As a result, it is not yet clear how to develop recommenda-
tions on using specific quantitative methods and relate them to inherent SCR properties.
This study aims to provide a comprehensive review of the quantitative analyses of SCR. Such a
review can be particularly beneficial for researchers who seek to develop analytical models for
SCR. The particular contribution of this paper is exploring and analyzing quantitative drivers of
SCR around the resilience capacity concept (Biringer et al. 2013, Hosseini and Barker 2016) that
is also used for analysis, classifications, and identification future research areas. The capacity re-
silience concept suggests building three lines of defense, which is close to the three level resilience
classification of LCN (low-certainty-need) SCs proposed by Ivanov and Dolgui (2019), i.e., para-
metric redundancy or absorptive capacity in the form of redundant inventory, process flexibility
or adaptive capacity in the form of backup suppliers established, and structural variety or restora-
tive capacity in the form of technology diversification. Such a combination is unique is SCR liter-
ature and explicitly incorporates a variety of decision-making dimensions at different levels of
disruption severity accounting for prioritizing investments in building and maintaining SCR. It
mimics the complexity of business reality affording more comprehensive understanding of SCR
and realistic application of quantitative methods for its analysis.
Firms usually encounter all three stages when coping with disruptions. Even if the methods of SC
resilience increase according to the three lines of defense visible in literature, they have been
mostly considered fragmented in previous surveys; we consolidate them, for the first time, into an
integrated framework. This paper also suggests and classifies several methodologies that can be
applied in the future to formulate and quantify SCR problems.  Our survey can be of value for
decision-makers and researchers since it proposes a structured analysis and recommendations as
to which quantitative methods to use, at different levels of defense, according to the capacity re-
silience concept. The usage of resilience capacity concept for SCR literature analysis is the unique
feature of this paper that differentiates it from the other existing quantitative surveys (Fahimnia et
al. 2015a, Ivanov et al. 2017b, Ribeiro and Barbosa-Povoa 2018).
The theoretical foundations of this study build on three main perspectives, namely:

---

## 第 6 页

1. Analyzing and visualizing existing SCR literature, particularly from an analytical and mathe-
matical modeling standpoint;
2. Reviewing and classifying the quantitative contributions of SCR based on capacity for resili-
ence; and
3. Identifying the gaps and limitations of current research and proposing potential research op-
portunities.
The paper is organized around these perspectives as follows. Section 2 presents the research meth-
odology of a structured literature review. An analysis of data visualization in current literature is
presented in Section 3. Section 4 is devoted to definitions and qualitative analysis of SCR litera-
ture, with a focus on factors of particular importance for quantitative models. Quantitative analysis
approaches to SCR and its measurement are presented in Section 5. Section 6 highlights current
gaps and future research opportunities. The paper is concluded in Section 7 with a summary of
major findings in research and their implications.
2. Research methodology of literature review
We conducted a systematic survey to evaluate the body of literature on SCR. This systematic lit-
erature review has been carried out through an iterative process of defining appropriate research
terms, reviewing the literature, completing analysis, and finalizing classification results. The de-
tails of the research methodology utilized in this paper are as follows:
1. Search methodology: The literature review considers publications about SCR over the last 15
years from 2002 to 2017. It includes definitions of SCR, quantitative and analytical modeling
of SCR, and follows an extensive, systematic search of academic peer-reviewed literature. The
review also contains both empirical and non-empirical studies, although the main focus is on
non-empirical results. An initial search was carried out through the Google Scholar and Scopus
citation databases to identify relevant papers. The list of papers was  obtained from different
publishers, including Elsevier (www.sciencedirect.com), Informs (http://pubsonline.in-
forms.org/),
Springer
(https://link.springer.com/),
Taylor
&
Francis
(http://www.tandfonline.com/),
Emerald
(www.emeraldinsight.com),
JSTORE
(http://www.jstore.org/),
Inderscience
(www.inderscience.com),
IEEE
(ieeex-
plore.ieee.org/xpl/periodicals.jsp/), and some library services (e.g., Engineering Village
www.engineeringvillage.com/). In order to ensure recent publications are covered in this liter-
ature review, the same procedure was implemented to locate papers published between 2016

---

## 第 7 页

and 2018 according to set keywords, as explained below. Information clustering has been car-
ried out using CiteSpace software (Chen 2016) to distinguish between the relevant and irrele-
vant categories of academic papers. Resilience is a multi-disciplinary concept that has been
widely receiving attentions by researchers from different disciplines. With the help of
CiteSpace, we were able to identify some clusters that are not relevant to the SCR papers such
as computer science and civil engineering.
2. Methodology implementation: The literature search was conducted using Boolean keywords
combinations “(SC vulnerability OR supply disruptions) AND (SC resilience OR SC resili-
ency)”. The keywords used were “SC resilience”, “resilience supplier”, “SC vulnerability”,
“supply disruptions”, “resilience”, “resilient supply”, “SC disruption”, “flexibility”, “resilience
distribution networks”, “supply resilience strategy”, “SC flexibility”, “resiliency in SC”, and
“enterprise resilience”.
3. Reviewing, refining, and filtering database: The papers identified in the search were then ana-
lyzed and evaluated by reviewing abstracts, then reading the full-text of each article. Irrelevant
papers were filtered out, based on academic judgment, after being read in full. We also utilized
information clustering techniques implemented using CiteSpace software to filter out irrelevant
papers. We scanned the references of papers that have been found through the searching process
to find relevant papers not identified through the search process. Reference chasing was also
performed to find relevant papers not identified through the search process. The reviewing,
refining, and filtering of papers not only established a breadth and width coverage, but also
captured important elements of the overall picture of SCR literature. In total, 168 papers are
reviewed in this study.
A block diagram of the methodology is illustrated in Figure 1.

---

## 第 8 页

Figure 1: The flowchart of literature-review methodology.
The outcomes of the literature review conducted allow for data visualization analysis, analysis of
geographic distribution of contributed organization, as well as category, journal and keyword in-
formation clustering.
3. Data visualization analysis of literature review
This section presents a visualization-based scientometric analysis to examine the current state and
explore developments in the field of SCR. Analyzing how data was visualized in literature using
visualization software has recently received a great deal of attention by researchers conducting
state of the art reviews, i.e., Fahimnia et al. (2015a), Li et al. (2017a), Yu and Xu (2017), Hosseini
et al. (2016a), Fahimnia et al. (2015b). The results of such an analysis help to answer the following
questions: 1) Which subject category is the most popular in the domain of SCR?; 2) Which journals
extensively publish about SCR?; 3) Organisations of which countries are most productive in pro-
ducing SCR research?; 4) What are emerging trends and developments in SCR research?
Searching on SCR
database
Category Cluster-
ing
Filtering based on Cat-
egory clustering
Analyzing abstracts and
filtering irrelevant papers
Filtering based on
Full-text Reading
Reference scanning
Analysis of literature
review

*（本页包含 5 张图片，请参阅原PDF）*

---

## 第 9 页

3.1. Geographical distribution of contributing organizations
An interesting bibliometric analysis is to uncover the geographical distribution of all organizations
(research institutes) contributing to SCR literature. We used BibExcel to analyze bibliographical
data in SCR research. Figure 2 illustrates the geographical distribution of all contributing organi-
zations. The size of the red circles is proportional to the contribution degree of each organization.
It becomes evident that U.S. research institutes have the highest contributions to SCR literature,
and remarkable that most of these are located on the east coast. Our findings indicate that England
and China are the second and third most productive in terms of SCR literature. The degree of
contribution from other countries can be seen in Figure 2. Notably, AGH University Science &
Technology from Poland is the most productive research institute, while MIT and Northwestern
University from the U.S. are the second and third most productive research institutes.
Figure 2: Geographical locations of all contributing organizations.
3.2. Category information clustering
An important analysis carried out in this study was to develop information clustering in SCR from
the perspective of categories. To do so, CiteSpace visualization software was utilized. CiteSpace
has been used by many researchers to visualize and analyze trends and patterns in literature (Yu

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 10 页

and Xu 2017; Chen et al. 2016; Xiang et al. 2017). Category information clustering, using
CiteSpace, helped us identify and exclude irrelevant papers, during our search process, such as
those concerning ecology and environmental science and food science and technology. For exam-
ple, Figure 3 depicts one snapshot of the visualization results from CiteSpace that demonstrates
clusters of papers. These clusters are comprised of papers which share the same keywords. The
size of the cluster is proportional to the number of papers that use the specific keyword represent-
ing the cluster. As a result, irrelevant papers could be filtered out according to keywords in the
category information clustering.
It should be noted that CiteSpace implements spectral clustering technique to identify clusters.
Generally speaking, spectral clustering outperforms traditional clustering methods such as k-
means or single linkage (Shi & Malik 2000, Luxburg 2006). For example, spectral clustering is
more flexible and robust and does not imply any assumptions on the forms and number of clusters
unlike the k-means clustering. Hence, the number of clusters is uniformly determined by the
spectral clustering algorithm based on the optimal cut method. It is notable that cluster labels are
based on the leywords and abstracts of citing papers determined by log-likelihood ratior (LLR).
More technical information about spectral clustering and LLR on co-citation clustering can be
found in (Chen et al. 2009).
Figure 3: Category information clustering

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 11 页

3.3. Keyword information clustering
Another visualization performed for this study was to analyze how frequently certain keywords
were used in SCR literature. The results illustrated in Figure 4 show that “SCR” is the main key-
word, followed by “management”, “performance”, “SC disruption”, “risk”, and “disruption”. For
greater specificity, a pairwise comparison between keywords used across SCR literature was ex-
amined. For example, Figure 4 shows that “SC resilience”, “management”, “performance”, and
“SC disruption” are the most common keywords used together across the SCR papers analyzed.
The thickness of the line between two given words denotes the degree of connection: a thicker line
means a greater frequency of connection. We found that “strategy” used in SCR papers refers to a
resilience strategy implemented before and after disruptive events. Literature has also extensively
dealt with “risk”, “flexibility”, and “framework” as the next most popular keywords used in tan-
dem with “SC resilience”.
Figure 4: Keyword information clustering of SCR research area.
3.4. Journal information clustering
We used CiteSpace to visually cluster the SCR literature, based on source of publication. Accord-
ing to the results represented in Figure 5, International Journal of Production Economics, Interna-
tional Journal of Logistics Management, International Journal of production Research, and Supply

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 12 页

Chain Management: An International Journal, are the top four cited journals contributing to the
SCR literature, followed by Journal of Business Logistics and MIT Sloan Management Review.
The analysis of journal clusters shows that Operations Research Journals, such as European Jour-
nal of Operational Research, Computers & Operations Research, Transportation Research-Part E,
and Decision Science, have smaller cluster size in comparison with journals, such as International
Journal of Logistics Management, International Journal of Physical Distribution & Logistics Man-
agement, MIT Sloan Management Review, and Journal of Business Logistics, which focus on the
qualitative aspect of SCR. This analysis emphasizes the need for more quantitative research on
SCR in the future.
Figure 5: Main journal clusters in SCR research area.
4. Definitions and qualitative analysis of SCR literature
Companies that operate at global scale with inherent uncertainty at the structural SC design level
have a common question to ask. How do some companies obtain better performance than others
under conditions of severe disruptions? In this section we introduce the notion of SCR in the
framework of resilience capacity. Resilience is a multidisciplinary concept that was initially dis-
cussed in sciences, such as psychology (Bonanno et al. 2005; Bonanno and Galea 2007), ecology
(Hartvisgen et al. 1998; Webb 2007; Kerkhoff and Enquist 2007), economics, and organizations
(Rose 2007; Hollnagel 2006). In ecology literature, resilience is loosely defined by Webb (2007)

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 13 页

as “the ability of the system to maintain its function when faced with novel disturbance”. More
generic definitions of resilience can be found in (Hosseini et al. 2016a).
The concept of SCR is relatively new, along with a broader focus of research in SC risk manage-
ment. SCR has been defined by various scholars. Christopher and Peck (2004) defined SCR as
“the ability of SC system to return to its original or move to a new, more desirable state after being
disrupted”. Sheffi and Rice (2005) defined SCR as “the firm’s ability to absorb disruptions or
enable the SC network to return to state conditions faster and thus has a positive impact on firm
performance”. Ivanov and Sokolov (2013) understand SCR as the ability to maintain and recover
(adapt) planned execution, as well as to achieve planned (or adapted, yet still acceptable) perfor-
mance. Appendix 1 summarizes a comprehensive list of SCR definitions proposed in recent liter-
ature.
Despite of variations in SCR definitions proposed, some commonalities can be observed. Defini-
tions shared several key elements, such as anticipating unforeseen disruptive events, withstanding
disruptions, responding quickly to disruptions, recovering from disruptions, and returning to
steady state conditions. Closs and McGarrell (2004) and Ponis and Koronis (2012) highlighted that
anticipating unexpected disruptions ensures better readiness and preparedness. Kim et al. (2015),
Pettit et al. (2010), and Closs and McGarrell (2004) stated that strengthening the capability of SC
firms to withstand disruptions is a key proactive strategy that makes SCs more resilient. Many
definitions underscore that the capability of a SC to recover and return to normal operations after
a disruption is an essential factor of resilience (Longo and Oren 2008; Falasca et al. 2008; Guoping
and Xinqiu 2010; Ponis and Koronis 2012; Roberta Pereira et al. 2014; Ponomarov 2012; Kama-
lahmadi and Mellat-Parast 2016; Govindan et al. 2016).
Although formal definitions of SCR do not appear to highlight the cost of a resilience strategy,
some researchers acknowledged the impact of cost-effectiveness in resilience practices. Christo-
pher and Rutherford (2004) highlighted that SCR can be accomplished efficiently and cost effec-
tively using the agile six sigma methodology. Haimes (2006) and Haimes et al. (2008) argued that
resilience not only aims to recover the desired states of a system within an acceptable time, but
also at an acceptable cost. Ivanov et al. (2014a,b, 2016, 2017a,b) discussed that disruptions should
be mitigated by means of cost-efficient recovery policies. Ivanov and Dolgui (2018) suggested a
new approach to SC disruption risk management, where SC behavior is less dependent on the
certainty of our knowledge about the environment and its changes, i.e., low-certainty-need (LCN)

---

## 第 14 页

SCs. Two efficiency capabilities of the LCN SC are a low need for uncertainty consideration in
planning decisions and a low need for recovery coordination efforts, based on a combination of
lean and resilient elements into SC resileanness.
4.2. SCR definition by the resilience capacity concept
In order to present our new definition of SCR, we first need to elaborate on the concept of resilience
capacity (Figure 6).
Figure 6:  Resilience capacity of supply chain systems with three lines of defense.
First and principally, resilience capacity is a new and important dimension of system performance
under uncertainty which consists of the resilience enhancement features that could increase the
ability of a system to absorb, adapt, and restore itself after disruption (Hosseini and Barker 2016c).
It is based on three lines of defense (Figure 6), which is close to the three level resilience classifi-
cation of LCN (low-certainty-need) SCs proposed by Ivanov and Dolgui (2019). Biringer et al.
(2013) introduced the concept of resilience capacity with three categories, each of which represents
temporal attributes before, during, and after a disruption: absorptive capacity, adaptive capacity,
and restorative capacity.
According to Biringer et al. (2013), absorptive capacity is the capability of a system to absorb or
withstand the impact of system perturbations and minimize the negative consequences of disrup-
tion with relatively low levels of energy or effort. Lücker et al. (2018) and Ivanov and Dolgui

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 15 页

(2019) refer to multiple sourcing, risk mitigation inventory and supplier segmentation as usual
resilience mechanism at this level. For example, PepsiCo uses a backup packing plant in the US
and carries a risk mitigation inventory to cope with the disruptions in coconut water supply from
South Asia (HBS 2017). Absorptive capacity refers to all implementations put in place prior to a
disruption occurring. Absorptive capacity can be thought of as the first line of defense against
disruptions that lessens the effort necessary to recover after a disruption occurs. While develop-
ment of absorptive capacity is desirable and indeed critical to withstand the disruptions, exploiting
the resilience capabilities to achieve the desired performance outcomes through effective adapta-
tion is becoming increasingly important (Ivanov and Sokolov 2013).
Adaptive capacity is defined by Biringer et al. (2013) as the degree to which a system can adapt
itself and attempt to overcome disruption by implementing nonstandard operating practices with-
out any recovery activities. Adaptive capacity is the second line of defense against disruption when
absorptive capacity is not sufficient to harness disruption. Hosseini and Barker (2016c) identified
quick evacuation of port, mode flexibility, and repositioning of containers at the port as primary
features of adaptive capacity for increasing the resilience of inland waterway ports. Biringer et al.
(2013) described reorganization as a key element of adaptive capacity of companies and SCs.
Transportation companies or industries like railroads may normally be prohibited to collaborate
with each other by antitrust law; however, temporary executive orders can be passed to give permit
collaboration to the railroad transportation companies in order to recover quicker in case of na-
tional disasters. Finding and re-routing a backup connection between customer and distribution
center is highlighted as an adaptive capacity in the case of disruption by Turnquist and Vugrin
(2013).
Restorative capacity is defined by Biringer et al. (2013) as the ability of a system to be restored
quickly and efficiently in the case if the absorptive and adaptive capacities of that system are not
able to maintain an acceptable level of performance. Restorative capacity is the third and last line
of defense when the system is broken and unable to perform. Hosseini and Barker et al. (2016c)
stated that budget restoration and resource restoration are two factors of restorative capacity for
ports.
Based on the notion of resilience capacity for a system, we define SCR as “SC capability to utilize
the absorptive capacity of SC entities to repulse and withstand the impacts of perturbations, to
minimize the consequences of disruptions and their propagation by utilizing adaptive capacity and

---

## 第 16 页

to recover performance level to normal operations in a cost-efficient manner using restorative
capacity when absorptive and adaptive capacities are not sufficient.”
Based on the definition of SCR presented above, we present a resilience hierarchy for SCR, as
illustrated in Figure 7.
Figure 7: The proposed hierarchy for SCR.
The hierarchal structure of SCR is compounded of four levels. The bottom level is occupied by
features of SCs which enhance resilience; these factors, such as surplus inventory at the manufac-
turer or having a backup supplier, will be discussed in detail in Section 5. Identifying resilience
enhancement features enables a better understanding of SCR. SC resilience enhancement features
make up the resilience capacity of an SC which, in turn, is comprised of absorptive, adaptive, and
restorative capacities. Vulnerability and recoverability of an SC are functions of resilience capacity
in the sense that SCs with higher capacity for resilience are less vulnerable to disruption and need
fewer recovery efforts. SCs with lower resilience capacity are more vulnerable and require more
effort to achieve recovery. Finally, SC resilience, located on the top level of the hierarchy, is a
function of the vulnerability and recoverability of the SC.
4.3. Conceptual drivers of SCR
Literature has extensively tried to identify the key characteristics and drivers of SCR from a qual-
itative point of view. In this subsection, we outline qualitative drivers that could improve the re-
silience of SCs. These drivers are identified by relevant authors who have identified, referred to,
or examined particular resilience strategies (proactive vs reactive). Key characteristics and ele-
ments considered are agility, visibility, flexibility, collaboration, information sharing (Blome et al.

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 17 页

2013, Bode and Macdonald 2017, Dubey et al. 2017, 2018).  Although sometimes these elements
have been used interchangeably by different authors, we attempt to explicitly specify them and to
identify the key drivers that contribute to building SCR taxonomy from the quantitative perspec-
tive.
4.3.1 Agility
Christopher and Lee (2004) argued that agility is one of the most powerful means of achieving
resilience in the SC. They stated that SC networks with higher agility are capable of more quickly
responding to turbulent conditions. Agility is defined as the ability of SC firms to respond quickly,
smoothly, and cost-efficiently to sudden changes in supply or demand (Wieland and Wallenburg
2013). Agility is also defined as a SC firm’s ability to respond promptly to unexpected market
changes and convert those changes to business opportunities (Jain et al. 2008). SC agility usually
refers to the SC ability to quickly adapt the network structure and operations policy to dynamic
and turbulent requirements of the customer (Dubey et al. 2018). Wieland and Wallenburg (2013)
stated that resilience is formed by two dimensions: agility, which is a reactive resilience strategy,
and robustness, which is a proactive resilience strategy. They highlighted that agility cannot only
enhance SC resilience, but also must have a positive effect on the value created for the SC cus-
tomer.
4.3.2 Visibility
Visibility is defined by Francis (2008) as “the identity, location and status of entities transiting the
SC, captured in timely message about events, along with the planned and actual dates/times of
these events.” SC visibility has also been defined as a transparent view of upstream and down-
stream inventories, demand and supply conditions, and production and purchasing schedules
(Christopher and Peck 2004). Saenz and Revilla (2014) discussed how SC visibility was beneficial
to improving Cisco’s resilience of their response to the Japanese tsunami and earthquake of 2011.
Although the Japanese tsunami and earthquake resulted in total economic losses of $217 billion,
Cisco suffered almost no revenue loss. Within 12 hours of the disaster occurring, Cisco was able
to identify all of its suppliers in the disrupted region, from tier 1 suppliers to suppliers of raw
materials, and within 24 hours was able to map its customers and field 118 inquiries (Saenz and
Revilla 2014). Chopra and Sodhi (2014) pointed out that visibility in SC entities is a key strategy
to protect SCs from disruptions. Visibility is a proactive strategy that contributes to SCR.
4.3.3. Flexibility

---

## 第 18 页

Erol et al. (2010) defined flexibility as the ability of firms and enterprises to adapt themselves to
changing environments and stakeholders with minimum effort and time. Millar (2015) argued that
flexibility, as a feature of SCR, determines a firm’s ability to respond to changes in the market,
such external impact being beyond the immediate scope and control of SC ecosystem. Rice and
Caniato (2003) recommended a hybrid flexibility approach to enhance SCR. Literature revealed
that flexibility practices, including flexible transportation, flexible sourcing, flexible labor arrange-
ment, and postponement, could all contribute to the resiliency of SCs (Tang 2006a; Tang 2006b;
Christopher and Holweg 2011; Pettit 2013). Christopher and Holweg (2011) argued that flexibility
makes SCs more resilient by enhancing rapid adaptability during turbulent conditions. In literature,
flexibility has been interchangeably used with the term “adaptive capability” (Soni et al. 2014).
Pettit et al. (2013) discussed that SCs with a lower level of flexibility in sourcing and order fulfill-
ment are more vulnerable to disruptions and less resilient.
4.3.4. Collaboration
Empirical and conceptual SCR literature has shown that collaboration is a key factor for building
resilient SCs (Christopher and Peck 2004; Juttner and Maklan 2011; Pettit et al. 2013). Although
there is agreement among researchers that collaboration can positively enhance SCR, it is not clear
exactly how collaboration influences SCR.
Collaboration in SC relates to the capability of two or more autonomous firms to work effectively
together, planning and executing SC operations toward common goals (Cao et al. 2010; Scholten
and Schilder 2015). According to a report released by BCI in 2013, 58% of SC disruptions origi-
nate from first tier suppliers and these suppliers are of the most concern for companies in terms of
sources or risk. Blackhurst et al. (2011) stated that collaboration between supplier and buyer can
significantly reduce the likelihood of SC disruption in the upstream SC and prevent the negative
impact of disruption propagation throughout the whole SC.
4.3.5. Information sharing
Information sharing is considered a key driver of SCR by some researchers (Soni et al. 2014; Datta
et al. 2007). Faisal (2010) argued that information sharing can help SCs to mitigate risk in the case
of disruptions. They suggest that exchanging and sharing between SC entities prior to and after a
disruption is necessary for the resiliency of the SC. Saghafian and Oyen (2012) pointed out that
information sharing coupled with emergency backup and storage facilities can make SCs more

---

## 第 19 页

resistant to disruptions and less vulnerable. Christopher and Peck (2004) argued that lack of infor-
mation sharing is a key source of SC vulnerability, because SC firms use forecast-driven rather
than demand-driven data, which prevents them from sharing information and eventually increases
the bullwhip effect.
Yang and Fan (2016) applied an approach based on integrating control theory and simulation to
show the impact of information-sharing on reducing the bullwhip effect under demand disruptions.
Brandon-Jones et al. (2014) analyzed survey data collected from 264 U.K. manufacturing compa-
nies and suggested that information sharing, along with SC connectivity, can improve SCR and
robustness. Li et al. (2017a) investigated the impact of incorporating information sharing across
different echelons of the SC to achieve higher resilience and mitigate uncertainty regarding sup-
plier capacity. Information availability is an important determinant in reliable/unreliable sourcing
literature and, more specifically, the availability of information to some players and the non-avail-
ability of this information to other players (Yang et al. 2009, Gupta and Sethi 2015).
5. Quantitative analysis of SCR
In this section, we use the concept of resilience capacity, introduced in Section 4, to classify the
analytical papers of SCR.
5.1. Absorptive capacity
5.1.1. Supplier segregation
Separating suppliers geographically can effectively reduce the disruption risk imposed on a man-
ufacturing facility, specifically in the event of a regional natural disaster. After the Japanese tsu-
nami and earthquake, which saw many auto-part suppliers on the east coast severely impacted,
several automakers, including Toyota, tried to work with geographically dispersed suppliers. Pur-
chasing raw materials from suppliers located in different regions could potentially reduce the like-
lihood of a regional natural disaster negatively affecting the suppliers of a manufacturing facility.
Hosseini and Barker (2016b) used Bayesian networks, a well-known statistical tool that works
based on conditional probability, to model the likelihood that a supplier would be separated from
a natural disaster zone. A supplier with a higher likelihood of separation from a disaster zone is
considered to be more resilient. The authors introduced three variables; segregation, tornado, and
flood. The likelihood that a supplier is separated from disaster is conditioned on the occurrence of
flood and tornado, as illustrated in Figure 8. The prior probability of flood and tornado occurrences

---

## 第 20 页

is modeled by truncated normal distribution. The variable for the marginal probability of segrega-
tion is obtained by a conditional IF statement. The authors stated that a supplier is considered to
be located in a disaster-safe zone if the occurrence probability of flood and tornado is less than
0.03, i.e., IF (probability of tornado and probability of flood <0.03, “True”, “False”). As shown in
Figure 8, the likelihood that the supplier is separated from the disaster zone (True state) is 65.76%.
Figure 8: Bayesian network modeling of supplier segregation from natural disaster.
Hosseini et al. (2018) used optimization methodology to consider segregation among suppliers.
The objective function is to maximize the smallest distance between the locations of any pair of
suppliers. Consider the following notations:
Input parameters:
𝑑𝑖𝑗: Shortest distance between locations of suppliers 𝑖 and 𝑗
𝐿: Smallest segregation distance between every pair of suppliers
𝑀: A constant large number
Decision variable:
𝑧𝑖: 1, if supplier i is assigned to the firm; and 0 otherwise
𝑍= 𝑀𝑎𝑥 ∑∑𝑧𝑖𝑧𝑗𝑑𝑖𝑗
𝑛
𝑗=𝑖+1
𝑛
𝑖=1
(1)
where
𝐿≤𝑑𝑖𝑗(1 + 𝑀(1 −𝑧𝑖) + 𝑀(1 −𝑧𝑗))     ∀𝑖, 𝑗∈𝑛| 𝑖< 𝑗
(2)
The model related to supplier separation is represented in Eqs. (1) and (2), where the objective
function is to maximize the segregation distance between suppliers. Hasani and Khosrojerdi (2016)
modeled facility dispersion and facility fortification as resilience strategy using a mixed-integer,
non-linear robust optimization model.

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 21 页

5.1.2. Multiple sourcing strategy
Evidently, sourcing strategies are of greater importance in achieving SCR (Yildiz et al. 2016, Yoon
et al. 2018). Namdar et al. (2017) developed a scenario-based mathematical model for SCR under
single and multiple sourcing. Their findings stress that, when decision-makers are risk-averse and
cautious, multiple sourcing results in better service level with a lower conditional value of risk
compared to single sourcing. Lücker and Seifert (2017) presented a mathematical model which
shows that, under some conditions, dual sourcing can be considered a substitute for risk mitigation
inventory at manufacturing sites in a pharmaceutical SC. The authors also show that an optimal
dual source production rate can greatly reduce disruption time. Bicer (2015) showed how Extreme
Value theory (EVT) can be applied to price the value of flexibility in the case of disruptive events.
The author investigated the impact of dual sourcing with a single product under conditions of high
demand fluctuation. The EVT was used to characterize the tail heaviness of demand distribution.
The author concluded that companies could potentially improve cost efficiency if customer de-
mand distribution is more heavy-tailed demand when the cost of sourcing from supplier is rela-
tively low.
Torabi et al. (2015) considered multiple sourcing in a mathematical model to select resilient sup-
pliers. Other researchers, including Peng et al. (2011); Sawik (2011), Sawik (2013), Meena and
Sarmah (2013), Sadghiani et al. (2015); Zhang et al. (2015); Kamalahmadi and Mellat-Parast
(2016), Ivanov et al. (2017a, b), and Ivanov (2018a) underline that manufacturing facilities must
reduce the supplier dependency and recognize the value of sourcing diversification by collaborat-
ing with multiple suppliers rather than a single supplier.
5.1.3. Inventory positioning
Tomlin (2006) highlighted the impact of inventory control strategies on mitigating disruption risk
in SC. Inventory strategies are part of the absorptive capacity of a supplier or manufacturer in
terms of ordering and stocking decisions. This fact needs to be taken into account prior to disrup-
tion. The resilience degree of a manufacturing facility does not depend on its initial capacity alone,
but also on its additional initial capacity. Some manufacturing companies prefer to reduce inven-
tory holding costs. Those who implement lean manufacturing principles may not carry excess in-
ventory at all, instead accepting the disruption risk and associated cost. Tomlin (2006) investigated
the impact of accepting disruption risk (acceptance strategy) and not carrying excess inventory in
a single-product supply system with two suppliers. He showed that the optimal mitigation strategy

---

## 第 22 页

can be achieved for short disruptions by utilizing the acceptance strategy, but holding excess in-
ventory could be an optimal strategy for rarer, but longer disruptions. Turnquist and Vugrin (2013)
formulated a stochastic optimization model to design resilient distribution networks. In this work,
it is assumed that each distribution center can carry excessive inventory in addition to the normal
holding inventory. The optimization model determines the additional initial inventory each distri-
bution center must carry prior to the disruption, to ensure that the total cost of initial additional
capacity at distribution centers is minimized. Khalili et al. (2016) considered an integrated produc-
tion-distribution planning problem in a two-echelon SC, where transportation links, distribution
centers, and active capacity levels of the production facilities are vulnerable to disruption and op-
erational risks. The authors proposed a two-stage scenario based on a mixed stochastic-possibilis-
tic programming model, where two types of inventory are taken into account: (1) additional initial
production capacity of the production facility, and (2) emergency inventory of a specific product
type in the distribution center. Elluru et al. (2017) also highlighted the impact of expanded inven-
tory at the distribution facility as a key mitigation strategy when designing resilient networks using
the location-routing problem.
Spiegler et al. (2012) studied automatic pipeline inventory and order-based production systems
using control engineering theory. The pipeline inventory is characterized by a feedback loop. The
integral of “time absolute error” is a measurement of resilience, which quantifies the error level
between actual and desired inventory after disruption. The authors analytically examined the trade-
off between the resilience level of inventory systems and the costs of inventory. The authors ex-
plored reduction of recovery time and work in progress using an ordering control algorithm: mov-
ing from a leveling strategy to a chase strategy can enhance resilience, but may increase the cost
of the SC. Barker and Santos (2010) applied an input-output model to evaluate the impact of dis-
ruption on SCR.
5.1.4. Multiple transportation channels
Khalili et al. (2016) investigated the impact of resilience enhancement under multiple transporta-
tion channels and rerouting options for an integrated production-distribution system. The impact
of availability and size of different transportation modes under different disruption scenarios are
analyzed. The authors concluded that utilizing multiple transportation channels in conjunction with

---

## 第 23 页

prepositioning of emergency inventory at distribution centers could significantly enhance the re-
silience and reduce the recovery time. Kamalahamadi and Mellat Parast (2016b) echoed those
results considering the impact of multiple transportation channels on the SCR.
5.2. Adaptive capacity
5.2.1. Backup supplier
In Fig. 9, we summarize the primary decisions of resilient SC design with supplier disruption con-
sideration.
Figure 9: Primary decisions of SCR with focus on supply vulnerability.
Contracting between a manufacturing facility and a backup supplier is a preparatory action that
can enhance SCR. Torabi et al. (2015) found that having a backup supplier is an effective strategy
to mitigate SC disruption. Hou et al. (2010) studied a scenario in which a buyer has two supply
options: an inexpensive, but vulnerable one (primary supplier), or a highly reliable, but expensive
one (backup supplier). The authors then considered a buy-back contract between the buyer and
backup supplier when the primary supplier has experienced a disruption. Chakraborty et al. (2016)
used game theory to mitigate SC disruption with random demand and price where suppliers are
prone to disruption. A backup supplier is incorporated into the model as a key, pre-disaster resili-
ence strategy. Using a rigorous quantitative methodology, Saghafian and Van Oyen (2016) inves-

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 24 页

tigated the impact of contacting a secondary flexible backup supplier on SC mitigation. The au-
thors measured the true value of a flexible backup supplier and determined the upper bounds for
the amount a risk-averse manufacturing plant should be willing to pay to implement a flexible
backup supplier strategy. Jabarzadeh et al. (2018) developed a multi-objective stochastic program-
ming model, where primary and backup suppliers are separately modeled as binary decision vari-
ables. The primary objective function of their model is to minimize the total cost of the SC under
different disruption scenarios, as represented in Eq. (3). Let’s consider the input parameters and
decision variables given below:
Input parameters:
𝑥𝑛: fixed cost of evaluating and selecting primary supplier n
𝑧𝑙:  fixed cost of contracting with backup supplier l
𝜋𝑠: probability of occurrence of disruption scenario s
𝛿𝑟𝑛: defective rate of primary supplier n for raw material type r
𝛾𝑟𝑙: defective rate of backup supplier l for raw material type r
𝑢𝑟𝑙𝑚: unit cost of purchasing raw material type r from backup supplier l and transporting it to
factory m
𝑞𝑟𝑛𝑚: unit cost of purchasing raw material type r from primary supplier n and shipping it to factory
m
Decision variables:
𝑋𝑛: a binary decision variable, equal to 1 if primary supplier n is selected, and 0 otherwise.
𝑍𝑙: a binary decision variable, equal to 1 if backup supplier l is selected, and 0 otherwise.
𝑄𝑟𝑛𝑚𝑠: quantity of raw material type r transported from primary supplier n to factory m under
scenario s
𝑈𝑟𝑙𝑚𝑠: quantity of raw material type r transported from backup supplier l to factory m under sce-
nario s
Min 𝑍= ∑𝑥𝑛𝑋𝑛+ ∑𝑧𝑙𝑍𝑙
𝑙∈𝐿
𝑛∈𝑁
+ ∑𝜋𝑠[∑∑∑𝑞𝑟𝑛𝑚𝑄𝑟𝑛𝑚𝑠
1 −𝛿𝑟𝑛
𝑚∈𝑀
𝑛∈𝑁
𝑟∈𝑅
+ ∑∑∑𝑢𝑟𝑙𝑚𝑈𝑟𝑙𝑚𝑠
1 −𝛾𝑟𝑙
𝑚∈𝑀
𝑛∈𝑁
𝑟∈𝑅
]
𝑠∈𝑆
(3)
The first and second terms of objective function are the cost of selecting primary and backup sup-
pliers, respectively, while the third term is the total cost of shipping raw materials from the primary

---

## 第 25 页

and backup suppliers to factories. It is notable that the model developed by Jabarzadeh et al. (2018)
determines primary and backup supplier decisions prior to disruption. Despite this work, Torabi et
al. (2015) developed a two-stage programming model where the primary suppliers are determined
in the first stage, prior to disruption, and the backup supplier is determined in the second stage,
post-disruption. Primary and backup suppliers can be determined prior to disruption, but the se-
lection of a backup supplier depends on the severity of impact of the disruption on the capacity of
the primary supplier. Hence, utilizing two-stage stochastic programming models that determine
backup suppliers in the post-disruption stage based on the lost capacity of primary suppliers seems
to be more appropriate. Turnquist and Vugrin (2013) developed a stochastic optimization model
to design resilient distribution networks. A backup supplier is modeled in the form of a set of
constraints that allow one backup connection for each customer, but do not force these connections
to be made. Kamalahmadi and Mellat-Parast (2015a) modeled a mixed integer linear programming
model where supplier flexibility, or the ability of a supplier to provide more items than initially
requested, is considered as a decision variable of mitigation strategy.
5.2.2. Rerouting
Redundancy within transportation networks in the event of a natural disaster could enable a SC to
use nonstandard and more expensive routing options to ensure continuity. For example, droughts
halted critical barge traffic on some portions of the Mississippi river in 2012. Many shipping com-
panies were forced to switch from waterway transport, one of the most inexpensive forms of long
distance bulk transportation, to railroad transport. Many cargo shipping companies may consider
rerouting options from a primary port to an alternative port if the primary one is congested due to
disruption. Liu and Lee Lam (2013) presented a simplified model of SCs with two echelons, sup-
plier and customers, connected through a transportation network with one primary port. The au-
thors investigated the impact of disruption at the primary port and the possibility of rerouting from
the supplier to an alternative port. Duration and frequency of disruption were modeled by a discrete
time Markov chain distribution. The Markov rewarding process-based methodology demonstrates
that the best performance, which includes minimal backlog, reasonable inland traffic, and a reliable
shipping schedule, can be achieved through a balance of contingency routing and capacity expan-
sion. Khaled et al. (2017) proposed an optimization model for rerouting under high congestion due
to disruption at links and nodes. Wang et al. (2016) examined the rerouting strategy to enhance
SCR from the supplier’s perspective. The authors developed a mathematical model that finds an

---

## 第 26 页

optimal rerouting strategy for multiple suppliers’ SC in terms of product allocation and supplier
selection. The findings of their model show that a higher level of resilience is achievable if a re-
routing strategy is carried out sooner.  Hosseini and Khaled (2016) developed a hybrid ensemble
and AHP for a resilient supplier selection problem. The authors considered rerouting and reorgan-
ization as two key factors of adaptive capacity.
5.2.3. Communication
Communication and cooperation are resilience enhancing features of adaptive capacity that help
SCs to overcome disruptions through appropriate communication and collaboration, in a timely
manner, among members of the SC. Although the role of communication among SC businesses
and enterprises is acknowledged by qualitative studies (Scholten and Scilder 2015; Mandal et al.
2016; Wieland and Wallenburg 2013), there are very few quantitative papers that explore the role
of communication in SCs. Reyes Levalle and Nof (2015a) studied supply network resilience as it
is influenced by network level interactions and communication with other agents. The authors used
collaborative control theory, where supply networks are modeled as a set of interconnected, au-
tonomous agents that interact to enable a flow of physical goods, tasks, and/or information, and a
set of control protocols that regulate the behavior of agents. The results show that communication
and collaboration among agents can help to effectively ensure resilient supply networks. In another
paper, Reyes Levalle and Nof (2015b) studied the impact of resilience by training (RBT) on SC
topology and resilience under random and targeted disruptions. The outcomes of their research
indicate that communication within SC networks not only can increase the service level of normal
business operations, but can also increase the post-disruption service level significantly.
5.2.4. Substitution
Substitution is the capability of a manufacturing facility to temporarily substitute raw material with
alternatives until operations return to a steady state. For example, consider a power SC where the
production capacity of a combined cycle power plant is affected by a shortage of natural gas.
Switching between natural gas and coal fuel could temporarily sidestep disruption of the power
supply. Of course, technical issues arising from raw material replacement must be considered by
the manufacturer prior to disruption. Mancheri et al. (2018) applied dynamic simulation to measure
the resilience of a tantalum SC. The authors argued that material substitution in product design
could enhance the resilience of tantalum SC.
5.3. Restorative capacity

---

## 第 27 页

Hosseini and Barker (2016b) discussed suppliers’ restoration budgets and technical resource res-
torations as two arms of restorative capacity, which significantly help suppliers to recover quickly.
The authors modeled these two factors using a BN approach for selecting resilient suppliers. Sa-
hebjamnia et al. (2015) proposed a multi-objective, mixed integer, linear programming (MOMILP)
model, where budget restoration availability is modeled as a restriction in the resource allocation
problem. Sahebjamnia et al. (2018) integrated disaster recovery planning with business continuity
to build organizational resilience. To do so, the authors developed a MOMILP, where external and
internal restoration resources of the manufacturing facility are taken into account. The authors
argued that reducing organizational resources, including human resources, facilities, and equip-
ment, can disrupt a number of critical functions of the manufacturing facility. Restoration level as
a time unit is considered a key variable of post-disaster strategy. Turnquist and Vugrin (2013)
proposed a stochastic, mixed integer, programming model to design resilient distribution centers
(DCs), where restoration capacity investment (unit/period) is considered a resilience-enhancing
feature of DCs.
5.4. Modeling and solution methodologies
Analyses performed in Sections 5.1-5.3 allow the modeling approaches considered to be divided
into four categories. These categories are as follows: Category I: mathematical and optimization
modeling; Category II: structural equations modeling; Category III: Bayesian networks; Category
IV: simulation techniques; Category V: multi-criteria decision-making.
The solution methodologies are divided into four main categories. Some researchers have tried to
solve optimization models using exact methods, which is difficult and limited in terms of large-
size problems. Some authors utilized exact solver commercial software like GAMS, CPLEX,
Lingo, AnyLogic, and anyLogistix. For large-scale problems, particularly stochastic programming
models with large numbers of disruption scenarios, meta-heuristic algorithms have been applied.
Multi-criteria decision-making, such as AHP, ANP, and VIKOR, has been used to evaluate the
performance of SC systems. Fuzzy logic and grey set theory are also used to deal with SCR prob-
lems. Examples of modeling and solution approaches are presented in Appendix 2.
Figure 10 summarizes the causal relationship between SCR capacity and its drivers. Here, we con-
sider a two-stage SC with manufacturer and supplier.  In Figure 9, each arrow is represented by
either a positive or negative sign. An arrow from factor A to factor B, with a positive sign, denotes
a positive relationship between those two factors, meaning that increase (decrease) in A will lead

---

## 第 28 页

to increase (decrease) in B subsequently, while a negative sign means that an increase in A leads
to a decrease in B, or vice versa. As is represented by the causal diagram, supplier resilience ca-
pacity is influenced by pre-disaster and post-disaster strategies. Absorptive capacity forms pre-
disaster (proactive) strategy, while adaptive and restorative capacity together form post-disaster
(reactive) strategy. The enhancement resilience drivers of absorptive, adaptive, and restorative ca-
pacities for supplier and manufacturer are illustrated. Among drivers of resilience capacity, there
are some drivers, including multiple sourcing, multiple transportation channels, surplus inventory
of manufacturer, and capacity expansion of supplier, that could influence SC sustainability.  From
the sustainability perspective, less inventory, single sourcing, and use of a single transportation
channel is more desirable than multiple channels.  As such, those factors enhance SCR, but may
not be the best features from the sustainability point of view.
Figure 10: Causal diagram of supply chain resilience capacity and its drivers.
Absoprtive
capacity
Adaptive
capacity
Absorptive capacity
of supplier
Absorptive capacity of
manufatcuring fim
+
+
Capacity expansion
of supplier
+
Reiliability and
availability of supplier
+
Physical
protection of site
+
Surplus
inventory
Physical protection of
manufatcuring site
+
+
Supplier segregation
(geographic distribution)
+
Raw material
substitution
Communication
Multiple transportation
channels
+
Adaptive capacity
of supplier
Adaptive capacity of
manufacturing firm
Multiple
sourcing
+
+
+
+
Backup
supplier
+
+
+
Rerouting
+
Reliability of
machineries and
equipment
+
Plant shutdown
+
Restorative
capacity
Restorative capacity
of manufacturing firm
Restorative
capacity of supplier
+
+
Restoration/startup
resources of
manufatcuring facility
+
Supplier recovery
resources
+
Technology
restoration
Manpower
restoration
+
+
+
+
Pre-disaster
(proactive) strategy
+
Post-disaster
(reactive) strategy
+
+
Supply chain
resilience capacity
+
+
Supply chain
sustainability
-
-
--

---

## 第 29 页

5.4. SCR metrics
The analysis of literature shows that resilience in the context of SC management is modeled and
quantified in two different ways. The first way is to develop metrics that quantify the SCR. These
metrics are usually bounded between [0, 1] and considered as objective functions that must be
maximized in addition to minimizing SC cost as primary objective. For example, Torabi et al.
(2015) developed a resilience metric that is a function of absorptive capacity (inventory pre-posi-
tioning), adaptive capacity (backup supplier), and restorative capacity (restoration of disrupted
supplier). Let’s assume that the amount of lost capacity recovered by inventory prepositioning,
backup supplier, and restoration of disrupted supplier is denoted by A, B, and C, respectively, and
that 𝐿𝑇𝐴, 𝐿𝑇𝐵, and 𝐿𝑇𝐶 denote the time of receiving items associated with the A, B, and C resilience
strategy. The loss of resilience 𝑅𝐸′ can be shown graphically as the shaded area in Figure 10 and
can be mathematically calculated by Eq. (4)
𝑅𝐸′ = 𝐴× 𝐿𝑇𝐴+ 𝐵× 𝐿𝑇𝐵+ 𝐶× 𝐿𝑇𝐶
(4)
It is clear that a lower value of 𝑅𝐸′ results in higher supply resilience. The authors then calculated the
resilience of the supply base by Eq. (5):
𝑅𝐸= 1 −
𝑅𝐸′
𝑄× 𝑇∗
(5)
where, Q is the total amount of items the  manufacturer needs from the supplier and 𝑇∗is the upper
bound on the length of the recovery process (Fig. 11).

*（本页包含 1 张图片，请参阅原PDF）*

---

## 第 30 页

Figure 11: The recovery process of disrupted supplier (Torabi et al. 2015).
Ojha et al. (2018) developed a metric to quantify the resilience as a measure of service loss after-
math of disruption. Suppose there are n nodes (suppliers) in the supply network, and the resilience
index of node n denoted by 𝑅𝐼𝑘 is measured by:
𝑅𝐼𝑘= 1 −
∑
(1 −𝑆𝐿𝑘𝑤
𝑆𝐿𝑘0)
𝑤𝑛
𝑤=𝑤0
(𝑤𝑛−𝑤0)
(6)
where 𝑤0 and 𝑤𝑛 are the weeks when disruption occurs at the SC node, and the time when disrup-
tion ends plus the time to recover from the disruption. 𝑆𝐿𝑘0 and 𝑆𝐿𝑘𝑤 are the service levels of node k
prior to and after the disruption. The similarity that can be observed across these two measures,
proposed by Torabi et al. (2015) and Ojha et al. (2018), is that resilience is calculated by 1 minus
fraction of loss, so both metrics are bounded between 0 and 1. Torabi et al. (2015) measured the
loss of supplier capacity, while Ojha et al. (2016) considered the loss of service level.
Despite the metrics developed by Torabi et al. (2015) and Ojha et al. (2018) that quantify the
resilience of the supply network, many researchers have not measured SCR directly, but rather
have tried to measure the drivers of resilience. Käki et al. (2015) developed a metric using Bayes-
ian models that measures the risk deduction in supply networks. The proposed metric is capable
of quantifying the impact of disruption propagation throughout multi-tier supply networks. The
authors argued that the risk deduction metric can help to identify vulnerable suppliers, and enhance
risk mitigation. Mogre et al. (2016) measured the SC vulnerability using a multi-input output eco-
nomic model for different mitigation strategies. Jabarzadeh et al. (2018) considered backup sup-
plier and surplus inventory as a resilience strategy to meet customer demand, and the costs asso-
ciated with utilizing backup supplier and holding surplus inventory to be minimized. Hosseini et
al. (2018) quantified SCR as a measure of supplier segregation that aims to select a set of geo-
graphically dispersed suppliers.
5.5. Objectives and decision variables in SCR Problems
The major objective in designing a resilient supply network is to strengthen the capability of SC
entities to withstand against disruptions and recover quickly from disruption with minimal costs
and efforts when they are disrupted. In this step, various objective functions and decision variables

---

## 第 31 页

were specified in the growing body of literature. In this section we summarize some objectives
and decision variables of SCR optimization problems (Fig. 12).
Objectives in SCR Problems
Economic (cost or
profit)
consideration
Vulnerability
(performance/
service loss)
consideration
Recovery time/
resource
consideration
Uncertainty
consideration
Resilience
enhancement
considerations (e.g.,
flexibility,
redundancy)
Figure 12: Objective functions of SCR
Consider the examples of objective functions in Fig. 12 more detailed.
First, the most common objective in the SCR optimization models is monetary (e.g., minimizing
the total cost or maximizing overall profit). Second, the vulnerability objective functions measure
the performance or service level loss in the SC (e.g., inventory capacity loss, lead time increment,
stock out rate, fill rate) due to the disruption. Third, in the recovery time/resource consideration,
vulnerability and recovery are two aspects of SCR. The optimization models generally aim at max-
imizing the recovery level of production capacity of disrupted manufacturer, or supply capacity of
supplier, distribution center or warehouse. Hereupon, minimizing the length of recovery time or
maximizing the recovery level of a disrupted SC entity is conceptualized as a primary objective of
SCR in optimization models by some researchers (Torabi et al. 2015; Kamalahmadi 2015; Cardoso
et al. 2015; Dixit et al. 2016; Khalili et al. 2016; Kaur and Singh 2016; Elluru 2017; Namdar 2017;
Duhadway et al. 2017; Shrivastara et al. 2017; Margolis 2018; Ni et al. 2018; Mohammed et al.
2018; Ojha et al. 2018; Sabouhi et al. 2018; Wang et al. 2018; Hosseini et al. 2019). Fourth, un-
certainty can be modeled in SCR problems in different ways: i) disruption uncertainty such as
aoccurrence likelihood of disruptive events like natural disasters, power outage, labor strikes, etc.,
ii) operational uncertainty such as the a likelihood of unmet demand and shortage on supplier’s
capacity. The analysis of literature shows that the majority of SCR problems are presented in the
form of stochastic scenario based optimization models in order to tackle demand and supply un-
certainty under different disruptive event scenarios (Turnquist and Vugrin 2013; Torabi et al. 2015;
Khalili et al. 2016; Namdar et al. 2017; Hosseini et al. 209; Morshedlou et al. 2018). Fifth and
finally, an important objective in the reviewed models is to enhance the resilience of SCs by max-
imizing the resilience enhancement drivers (e.g., flexibility, redundancy, reliability) of SC entities.

---

## 第 32 页

Backup capacity of supplier and emergency inventory of manufacture are considered as two key
drivers of resilience enhancement features to meet customer demand by Turnquist and Vugrin
2013; Garcia_Herreros et al. 2014; Kamalahmadi & Mellat-Parast 2015; Sahebjamnia et al. 2015;
Torabi et al. 2015; Namdar et al. 2017; Rezapour et al. 2018; Sahebjamnia et al. 2018; Fahimnia
et al. 2018; Sahebjamnia et al. 2018; Sawik2018).
6. Current gaps and future research opportunities
In this section, we suggest potential research opportunities based on analysis of the research gap
and existing limitations in the SCR literature.
6.1. Mathematical modeling
Two-stage stochastic programming is one of most appropriate ways to deal with uncertainty orig-
inating from disruption. The decision variables in the first stage are related to the absorptive ca-
pacity of SCs, such as the level of prepositioned inventory at the supplier/manufacturer, or addi-
tional capacity carried by the supplier/distribution center. The second stage is scenario-based and
helps to determine whether a backup supplier should be used, and the quantity of items that should
be shipped from the backup and primary suppliers to the customer or manufacturer. Future at-
tempts can be made to develop two-stage stochastic models, where the objective function of the
model is to minimize the traditional SC cost (procurement cost + supplier evaluation cost + trans-
portation costs, etc.), and the second-stage objective function measures the resilience of the SC
under all possible disruption scenarios. Analyses of SCR literature show that robust optimization
has not been well-studied. Hence, exploring robust optimization modeling in the context of SCR
might result in interesting findings.
6.2. Bayesian network (BN) modeling
BN is a powerful methodology for handling uncertainty, risk assessment, and decision-making.
BNs are structured based on conditional probability and Bayes’ theorem, which captures the de-
pendency between different suppliers or between supplier and manufacturer in a supply network.
The likelihood that a manufacturing facility fails to operate due to failure at the supplier can be
modeled by BNs. An important challenge in large interconnected and complex supply networks is
to control the ripple effect. The ripple effect can occur when the impact of disruption propagates
throughout the entire SC and cascades downstream, rather than remaining localized or being con-
tained to only one part of the SC. Forward and backward propagation analysis is a unique feature

---

## 第 33 页

of BNs that does not exist in any other methodology, including regression models, structural equa-
tion modeling, or neural network modeling that captures the relationships among variables. Using
forward propagation analysis, we can enter any number of disruption observations and use propa-
gation to update the marginal probabilities of all unobserved variables. Forward and backward
propagation analysis can be used in the future to analyze the ripple effect in complex supply net-
works with a large number of nodes and links.   Lists of successful applications of BNs in the field
of risk assessment can be found in (Garvey et al. 2015; Hosseini and Barker 2016b; Hosseini and
Barker 2016c; Hosseini and Barker 2016c; Qazi et al. 2017; Qazi et al. 2018).
6.3. Markov chain modeling
Resilience is a stochastic and time-dependent concept, which is a function of systems’ vulnerabil-
ity and recoverability. The multi-state Markov process is a good way to model the vulnerability
and recoverability of SC elements, such as ports, suppliers, and manufacturing facilities. A dis-
crete-time, Markov chain process for a port with three states is represented in Figure 13.
1
2
3
α1
α2
α3
β1
β3
β2
Figure 13: A discrete time Markov chain model with three states simulating the operational ca-
pacity of the port.
State 1 represents the operational capacity of the port under normal conditions (prior to disruption),
state 3 represents the state of the port when it is fully disrupted, and state 2 is an intermediate state,
i.e., the port is partially disrupted or 50% of the port’s operational capacity is disrupted. In Figure
11, 𝛼1 represents the probability that the port absorbs the shock of disruption without losing oper-
ational capacity. 𝛼2 represents the probability that the port loses 50% of its operational capacity
due to disruption, while 𝛼3 represents the probability that the system will be fully disrupted. The
recoverability probability between the different states is represented by 𝛽1, 𝛽2, 𝛽3.
6.4. Multi-criteria decision-making

---

## 第 34 页

Although multi-criteria decision-making (MCDM) methods have been applied to the resilient sup-
plier selection problem by some researchers (Kull and Talluri 2008; Yoon et al. 2016; Lima-Junior
and Carpinetti 2016; Mizgier et al. 2017; Amindoust 2018), MCDM methods, such as TOPSIS,
AHP, ANP, ELECTRE, VIKOR, have not been well-studied in the context of SCR.  Future re-
search works could focus on exploring the applications of MCDM methods on resilient supplier
and vendor problems. MCDM would also be useful for evaluating SC networks with respect to
resilience, green, and organizational criteria, simultaneously.
6.5. Dynamic versus static modeling
As we discussed earlier, the degree of resilience in a system is a function of its vulnerability and
recoverability. A disrupted system bounces back to its steady state over a period of time (recovery
time) after the disruption. . Few of the current mathematical models in SCR literature considered
the dynamicity of resilience. Future optimization models are expected to consider time periods
prior to and after disruption. In addition to this, we observed very few papers that consider time
recovery constraints. Time and budget recovery constraints are among the most important re-
strictions on recovery operations in practice.  Because the problem statements concerning SC dis-
ruptions deal with time-dependent settings, which include dynamic inventory control, transporta-
tion control, sourcing control, and production control policies, the simulation methodology for the
given problem domain has earned an important role in academic research (Ivanov 2017a,b,
2018a,b). In comparison to analytical, closed-form analysis, simulation has the advantage of being
able to handle complex problem settings with situational behavior changes in the system over time.
This is inevitable in considering dynamic changes in production-ordering policies and SC design
structures (Ivanov and Rozhkov 2017).
6.6. Ripple effect and low-certainty-need (LCN) SC designs
The ripple effect manifests itself when the impact of a SC disruption cannot be localized and cas-
cades downstream, resulting in a high impact effect on SC performance (Dolgui et al. 2018). Anal-
ysis of the ripple effect in the framework of SCR is a promising research avenue. Low-certainty-
need (LCN) SC designs suggest a new approach to disruption risk management where SC behavior
is less dependent on the certainty of our knowledge about the environment and its changes (Ivanov
and Dolgui 2018). Structural variety, process flexibility, and parametrical redundancy are key LCN
SC characteristics that ensure efficient disruption resistance, as well as recovery resource alloca-
tion. Two efficiency capabilities of the LCN SC are low need for uncertainty consideration in

---

## 第 35 页

planning decisions and low need for recovery coordination efforts based on a combination of lean
and resilient elements. Future research in bridging LCN and resilience will allow the identification
of an LCN SC framework, as well as concepts and technologies for its implementation. Special
focus might be directed on digital technology in the implementation of an LCN framework.
6.7. Hybrid approaches using digital technologies
Industry 4.0 has received much attention in recent years, but only a few efforts have been made to
design resilient digital technology and Industry 4.0. There are few works that assess the impact of
Industry 4.0 and digital technology on SC risks (e.g., Ivanov et al. 2016; Ivanov et al. 2018b) and
analytics and SC risks (Choi and  Lambert 2017, Choi et al. 2017). Industry 4.0-driven SCs could,
potentially, be vulnerable because of the integration of cyber-physical systems, additive manufac-
turing, robotics, high-performance computing, cognitive technologies, and advanced materials. At
the same time, digital technologies could provide new ways to reduce disruption risks (Ivanov et
al. 2018b). Developing resilience strategies based on recovery and vulnerability measures of In-
dustry 4.0-driven decentralized SC designs is an interesting direction for research.
6.8. Integrating resilience and sustainability
As SCs become more complex and more operations are being outsourced, managing disruption
risks and achieving resilience have become more critical. Global SCs and transportation networks
form the backbone of the modern economy and directly influence such sustainability issues as
fueling trade, green consumption, employment rates, etc. A desirable SC design should consider
not only sustainability issues, such as awareness of environmental protection and social responsi-
bilities, but also consider the proactive and reactive resilience strategies in the case of disruptions.
Although there are perceptible intersections between resilience and sustainability issues, very few
papers, such as Fahimnia and Jabarzadeh (2016), have studied the interface of resilience and sus-
tainability.
SCR enhancements, in practice,  are driven by utilizing the backup supplier, capacity buffer, sur-
plus inventory, and multiple sourcing, while using single sourcing, less stored inventory, and less
redundancy (e.g., multiple transportation systems) are more important for sustainability (Ivanov
2018a). Future research works should aim for bridging resilience and sustainable issues by devel-
oping stochastic, multiple objective optimization models capable of making  trade-offs between
sustainable and resilience decisions.
6.9. Digital supply chain twins to improve resilience

---

## 第 36 页

A combination of simulation, optimization and data analytics constitutes a full package of tech-
nologies to create a digital SC twin – a model that always represents the state of the network in
real-time (Ivanov et al. 2018b). At each point of time, a digital twin represents the physical SC
with the actual transportation, inventory, demand, and capacity data and can be therefore used for
planning and real-time control decisions. If there is a strike at an international logistics hub, this
disruption can be spotted by a risk data monitoring tool and transmitted to the simulation model
as a disruptive event. Then, simulation in the digital twin can help show disruption propagation
and quantify its impact. In addition, simulation enables efficient recovery policy testing and the
adaptation of contingency plans according to the situation – for example, reconsidering alternative
network topologies and back-up routes on-the-fly. Since a digital twin can represent the network
state for any given moment in time, it allows for complete end-to-end SC visibility to improve
resilience and test contingency plans.
7. Discussion and Conclusions
In this paper, a systematic literature review of SCR was presented, aimed at identifying resilience-
enhancing features of SCs and understanding analytical approaches, especially mathematical mod-
eling of SCR problems. We presented a new definition for SCR, based on the resilience capacity
of SCs. We reviewed both the qualitative and quantitative drivers of SCR.   We classified quanti-
tative drivers that contribute to the resilience of SCs based on resilience capacity, which was fur-
ther divided into absorptive capacity, adaptive capacity, and restorative capacity. Absorptive and
adaptive capacities are the first and second lines of defense for SC systems and measure the inter-
nal capability of a SC to withstand disruption, while restorative capacity is the third line of defense
and measures the exogenous capability of SC. Different quantitative methodologies for modeling
SCR are reviewed. The objective functions, decision variables, and constraints of mathematical
models of SCR problems are discussed.
Some significant contributions emerge. The analysis of optimization models of SCR models show
that future research efforts could explore multi-objective optimizations with primary objectives,
such as minimizing total SC cost (e.g., sum of supplier evaluation cost, transportation cost, pro-
duction cost) and secondary objectives, such as maximizing the resilience of the SC or minimizing
the recovery time of a disrupted component of the SC. We predict that future OR models will focus
on developing multi-objective, two-stage stochastic programming, where some decisions should
be made in the first stage, prior to disruption, such as (i): who are the selected suppliers; (ii): how

---

## 第 37 页

much surplus inventory should a selected supplier carry prior to disruption; (iii): how many prod-
ucts should be transported from a selected supplier. The second stage should determine those de-
cision variables that depend on the disruption scenario and are determined after realization of dis-
ruption, such as (i) selection of backup suppliers; (ii) proportion of customer demand that can be
met by backup supplier due to disruption at the primary supplier; (iii) restoration capacity of dis-
rupted primary supplier. Of course, decision variables can be differentiated depending on the struc-
ture and components of the given SC.
Finally, we recommended potential future research avenues, which are divided into two classes:
methodology-based and subject-based. From the methodology side, future research efforts could
explore the applications of Markov chain modeling, Bayesian network, optimization models, and,
particularly, multi-objective, two-stage stochastic programming models of the SCR problem. From
the subject side, exploring the interface between green and resilience SCs, as well as the effect of
achieving resilience in Industry 4.0 and using digital technology, would be highly beneficial.

---

## 第 38 页

Appendix 1: Definitions of SCR.
Authors/year
SCR definition
Rice and Caniato (2003)
The ability of SC to react to unexpected disruption and restore normal supply net-
work operations.
Christopher and Peck
(2004)
The capability of SCs to operate in the face of disturbances and disruptions with
or without a limited decrease in their performance.
Gaonkar and Viswanad-
ham (2007)
The ability of a SC to maintain, resume and recover operations aftermath of a
severe disruptive event.
Falasca et al. (2008)
The capability of SC to reduce the likelihood of disruption, to reduce the conse-
quences of those disruptions when they occur and to reduce the time to recover
normal performance.
Ivanov and Sokolov
(2013)
The ability to maintain, execute and recover (adapt) the planned policies along
with achievement of the planned (or adapted, but yet still acceptable) perfor-
mance.
Longo and Oren (2008)
The capability of chain to respond to external/internal disruptions and vulnerabil-
ities, and quickly recovering an equilibrium state capable of guaranteeing high
performance and efficiency levels.
Ponomarov and Hol-
comb (2009)
Ability of SC to prepare for unexpected events, respond to disruptions, and restore
from them by maintaining continuity of operations at the desired level of connect-
edness and control over structure and function.
Pettit et al. (2010)
The ability of chain to withstand, adapt and grow in the face of turbulent changes.
Guoping and Xinqiu
(2010)
The ability of SC to return to its original status under emergency risk environment.
Barroso et al. (2011)
The ability of chain to react to the negative effects caused by disturbances that
occur at a given moment in order to maintain the SC’s objectives.
Ponis and Koronis
(2012)
The ability of SC to proactively plan and design the SC network for anticipating
unexpected disruptive events, respond adaptively to disruptions while maintaining
control over structure and function and transcending to a robust state of opera-
tions.
Kim et al. (2015)
A network-level attribute to withstand disruptions that may be triggered at the
node or arc level.
Kamalahmadi and Mel-
lat-Parast (2016)
The adaptive capability of a SC to reduce the probability of facing sudden disturb-
ances, resist the spread of disturbances by maintaining control over structures and
functions, and recover and respond by immediate and effective reactive plans to
transcend the disturbance and restore the SC to a robust state of operations.

| Authors/year | SCR definition |
| --- | --- |
| Rice and Caniato (2003) | The ability of SC to react to unexpected disruption and restore normal supply net- work operations. |
| Christopher and Peck (2004) | The capability of SCs to operate in the face of disturbances and disruptions with or without a limited decrease in their performance. |
| Gaonkar and Viswanad- ham (2007) | The ability of a SC to maintain, resume and recover operations aftermath of a severe disruptive event. |
| Falasca et al. (2008) | The capability of SC to reduce the likelihood of disruption, to reduce the conse- quences of those disruptions when they occur and to reduce the time to recover normal performance. |
| Ivanov and Sokolov (2013) | The ability to maintain, execute and recover (adapt) the planned policies along with achievement of the planned (or adapted, but yet still acceptable) perfor- mance. |
| Longo and Oren (2008) | The capability of chain to respond to external/internal disruptions and vulnerabil- ities, and quickly recovering an equilibrium state capable of guaranteeing high performance and efficiency levels. |
| Ponomarov and Hol- comb (2009) | Ability of SC to prepare for unexpected events, respond to disruptions, and restore from them by maintaining continuity of operations at the desired level of connect- edness and control over structure and function. |
| Pettit et al. (2010) | The ability of chain to withstand, adapt and grow in the face of turbulent changes. |
| Guoping and Xinqiu (2010) | The ability of SC to return to its original status under emergency risk environment. |
| Barroso et al. (2011) | The ability of chain to react to the negative effects caused by disturbances that occur at a given moment in order to maintain the SC’s objectives. |
| Ponis and Koronis (2012) | The ability of SC to proactively plan and design the SC network for anticipating unexpected disruptive events, respond adaptively to disruptions while maintaining control over structure and function and transcending to a robust state of opera- tions. |
| Kim et al. (2015) | A network-level attribute to withstand disruptions that may be triggered at the node or arc level. |
| Kamalahmadi and Mel- lat-Parast (2016) | The adaptive capability of a SC to reduce the probability of facing sudden disturb- ances, resist the spread of disturbances by maintaining control over structures and functions, and recover and respond by immediate and effective reactive plans to transcend the disturbance and restore the SC to a robust state of operations. |

---

## 第 39 页

Authors
Modeling approach
Software technology
Type of model
Vulnerable part
Key Drivers of SCR
Brusset and Teller (2017)
Structural equations modeling
-
Deterministic
Supply
Flexibility, external and integration capabilities
Carvalho et al. (2012)
Discrete event simulation
-
Stochastic
Supply and manufacturing fa-
cility
Additional stock (redundancy in inventory), restructur-
ing existing transport (flexibility in transportation)
Chowdhury and Quaddus
(2017)
Dynamic capability theory
-
Deterministic
Supply
Reverse capacity, flexibility, financial strength
Dixit et al. (2016)
Bi-objective programming
NSGAII + Co-kriging
Deterministic
Supply network
Surplus capacity of supplier
Hosseini and Barker (2016b)
Bayesian network
-
Stochastic
Supply
Geographic segregation, backup supplier, surplus in-
ventory, physical protection, rerouting, technical re-
source, budget resource
Hosseini and Khaled (2016)
Hybrid ensemble and AHP
-
Deterministic
Supply
Backup supplier, surplus inventory, reliability of sup-
plier, rerouting, raw material replacement
Hosseini et al. (2016d)
Bayesian network
-
Stochastic
Supply and manufacturing fa-
cility
Reliability, supplier separation, production restoration,
plant shutdown
Ivanov (2017)
Simulation
anyLogistix
Stochastic
Supply
Multiple sourcing, facility fortification
Ivanov and Rozhkov (2017)
Discrete-event simulation
AnyLogic
Stochastic
Supply
Production-ordering policy
Ivanov et al. (2014)
Dynamic control
-
Stochastic
Supply
Flexibility, surplus inventory
Ivanov et al. (2014b)
Hybrid optimal control-mathemati-
cal programming
CPLEX
Deterministic
Supply, Distribution centers
Backup sources, rerouting
Jabarzadeh et al. (2018)
Bi-objective stochastic program-
ming
GAMS/CPLEX
Stochastic
Supply and manufacturing fa-
cility
Backup supplier, production capacity of factory
Kamalahmadi and Mellat-
Parast (2015)
Stochastic programming
CPLEX
Stochastic
Supply
Flexibility of supplier’s capacity
Kammalahmadi and Mellat
Parast (2017)
Two stage stochastic programming
-
Stochastic
Supply
Backup supplier, pre-positioning inventory
Khalili et al. (2016)
Bi-objective two stage stochastic
programming
GAMS/CPLEX
Stochastic
Production capacity
Surplus inventories, transportation capacity
Liu et al. (2018)
Structural equations modeling
-
Deterministic
Manufacturing facility
Agility, integration
Mancheri et al. (2018)
Dynamic simulation
-
Stochastic
Supply and manufacturing fa-
cility
Resistance, rapid recovery, flexibility
Margolis et al. (2018)
Bi-objective programming
Gurobi
Deterministic
Manufacturing facility
Surplus capacity of manufacturing facility
Namdar et al. (2017)
Two-stage stochastic programming
GAMS/CPLEX
Stochastic
Supply
Multiple sourcing, backup supplier, spot purchasing
Pramanik et al. (2017)
AHP+TOPSIS+QFD
-
Fuzzy
Supply
Surplus capacity, responsiveness
Sahebjamnia et al. (2018)
Bi-objective robust possibilistic
programming
Epsilon constraint
Stochastic
Manufacturing facility
Restoration resource, budget recovery
Spiegler et al. (2012)
Control engineering
-
Stochastic
Supply
Inventory stock level
Torabi et al. (2015)
Bi-objective two stage stochastic
programming
Differential evolution algo-
rithm
Stochastic
Supply
Backup supplier, surplus capacity of supplier,
Turnquist and Vugrin (2013)
Stochastic programming
Lingo
Stochastic
Distribution centers
Extra capacity of distribution center (DC), restoration
capacity of DC, additional connections between DC
and customers
Hasani and Khosrojerdi (2016)
Mixed integer, non-linear robust
programming
Taguchi based memetic al-
gorithm
Deterministic
Supplier, manufacturer and
warehouse
Multiple sourcing, facility dispersion, facility rein-
forcement
Ojha et al. (2018)
Bayesian network
-
Stochastic
Supply
Backup inventory
Appendix 2: Examples of solution approaches and technology for SCR modeling
* It is notable that papers without a specific software technology are marked by “-”. *

| Authors | Modeling approach | Software technology | Type of model | Vulnerable part | Key Drivers of SCR |
| --- | --- | --- | --- | --- | --- |
| Brusset and Teller (2017) | Structural equations modeling | - | Deterministic | Supply | Flexibility, external and integration capabilities |
| Carvalho et al. (2012) | Discrete event simulation | - | Stochastic | Supply and manufacturing fa- cility | Additional stock (redundancy in inventory), restructur- ing existing transport (flexibility in transportation) |
| Chowdhury and Quaddus (2017) | Dynamic capability theory | - | Deterministic | Supply | Reverse capacity, flexibility, financial strength |
| Dixit et al. (2016) | Bi-objective programming | NSGAII + Co-kriging | Deterministic | Supply network | Surplus capacity of supplier |
| Hosseini and Barker (2016b) | Bayesian network | - | Stochastic | Supply | Geographic segregation, backup supplier, surplus in- ventory, physical protection, rerouting, technical re- source, budget resource |
| Hosseini and Khaled (2016) | Hybrid ensemble and AHP | - | Deterministic | Supply | Backup supplier, surplus inventory, reliability of sup- plier, rerouting, raw material replacement |
| Hosseini et al. (2016d) | Bayesian network | - | Stochastic | Supply and manufacturing fa- cility | Reliability, supplier separation, production restoration, plant shutdown |
| Ivanov (2017) | Simulation | anyLogistix | Stochastic | Supply | Multiple sourcing, facility fortification |
| Ivanov and Rozhkov (2017) | Discrete-event simulation | AnyLogic | Stochastic | Supply | Production-ordering policy |
| Ivanov et al. (2014) | Dynamic control | - | Stochastic | Supply | Flexibility, surplus inventory |
| Ivanov et al. (2014b) | Hybrid optimal control-mathemati- cal programming | CPLEX | Deterministic | Supply, Distribution centers | Backup sources, rerouting |
| Jabarzadeh et al. (2018) | Bi-objective stochastic program- ming | GAMS/CPLEX | Stochastic | Supply and manufacturing fa- cility | Backup supplier, production capacity of factory |
| Kamalahmadi and Mellat- Parast (2015) | Stochastic programming | CPLEX | Stochastic | Supply | Flexibility of supplier’s capacity |
| Kammalahmadi and Mellat Parast (2017) | Two stage stochastic programming | - | Stochastic | Supply | Backup supplier, pre-positioning inventory |
| Khalili et al. (2016) | Bi-objective two stage stochastic programming | GAMS/CPLEX | Stochastic | Production capacity | Surplus inventories, transportation capacity |
| Liu et al. (2018) | Structural equations modeling | - | Deterministic | Manufacturing facility | Agility, integration |
| Mancheri et al. (2018) | Dynamic simulation | - | Stochastic | Supply and manufacturing fa- cility | Resistance, rapid recovery, flexibility |
| Margolis et al. (2018) | Bi-objective programming | Gurobi | Deterministic | Manufacturing facility | Surplus capacity of manufacturing facility |
| Namdar et al. (2017) | Two-stage stochastic programming | GAMS/CPLEX | Stochastic | Supply | Multiple sourcing, backup supplier, spot purchasing |
| Pramanik et al. (2017) | AHP+TOPSIS+QFD | - | Fuzzy | Supply | Surplus capacity, responsiveness |
| Sahebjamnia et al. (2018) | Bi-objective robust possibilistic programming | Epsilon constraint | Stochastic | Manufacturing facility | Restoration resource, budget recovery |
| Spiegler et al. (2012) | Control engineering | - | Stochastic | Supply | Inventory stock level |
| Torabi et al. (2015) | Bi-objective two stage stochastic programming | Differential evolution algo- rithm | Stochastic | Supply | Backup supplier, surplus capacity of supplier, |
| Turnquist and Vugrin (2013) | Stochastic programming | Lingo | Stochastic | Distribution centers | Extra capacity of distribution center (DC), restoration capacity of DC, additional connections between DC and customers |
| Hasani and Khosrojerdi (2016) | Mixed integer, non-linear robust programming | Taguchi based memetic al- gorithm | Deterministic | Supplier, manufacturer and warehouse | Multiple sourcing, facility dispersion, facility rein- forcement |
| Ojha et al. (2018) | Bayesian network | - | Stochastic | Supply | Backup inventory |

---

## 第 40 页

Appendix 3: Summary of main SCR key drivers, classified in terms of absorptive capacity, adaptive capacity and restorative capacity.
Absorptive Capacity
Reference
Key drivers
Explanation
Hosseini and Barker (2016); Hosseini et al.
(2019)
Geographic distribution
Collaborations of manufactures with geograph-
ically dispersed suppliers increase the risk of sup-
ply discontinuity.
Tomlin (2006); Spiegler et al. (2012); Ivanov
et al. (2014a); Turnquist and Vugrin (2013);
Sawik (2013); Torabi et al. (2015); Sahebjam-
nia et al. (2015); Kamalahmadi and Mellat
Parast (2016b); Kamalahmadi and Mella
Parast  (2017); Khalili et al. (2016); Elluru et
al. (2017); Ivanov (2018a); Rezapour et al.
(2018); Jabarzadeh et al. (2018); Ivanov et al.
(2018); Lücker et al. (2018); Sawki (2018);
Tan et al. (2019)
Emergency inventory of manufacturer
and backup capacity of supplier
Backup capacity and emergency inventory could
reduce vulnerability of SC and enhance the SC’s
resilience.
Sawik (2011); Sawik (2013); Sadghiani et al.
(2013); Meena and Sarmah (2013); Zhang et
al. (2015); Bicer (2015); Torabi et al. (2015);
Namdar et al. (2017); Lücker and Seifert
(2017) ; Ivanov et al. (2017a,b); Ivanov
(2018a)
Multiple sourcing strategy
Multiple sourcing strategy has a higher level of as-
sociation with SCR as compared with single sourc-
ing strategy.
Hosseini and Barker (2016c); Hosseini et al.
(2019)
Maintenance and reliability
Manufacturers could improve their resilience by
collaborating with reliable suppliers with lower dis-
ruption rates.
Khalili et al. (2016); Kammalahmadi and
Mellat Parast (2016b)
Multiple transportation channels
Utilizing multiple transportation channels could en-
hance the SCR in the case of transportation dam-
ages.
Adaptive Capacity
Reference
Key drivers
Explanation
Hou et al. (2010); Turnquist and Vugrin
(2013); Torabi et al. (2015); Chakraborty et
al. (2016); Saghafian and Van Oyen
(2016);Hosseini and Barker (2016b); Kama-
lahmadi and Mellat Parast (2017); Jabarzadeh
et al. (2018)
Backup supplier
Utilizing backup supplier when facing a disruption
may improve the SCR

|  | Absorptive Capacity |  |  |  |
| --- | --- | --- | --- | --- |
| Reference |  | Key drivers | Explanation |  |
| Hosseini and Barker (2016); Hosseini et al. (2019) |  | Geographic distribution | Collaborations of manufactures with geograph- ically dispersed suppliers increase the risk of sup- ply discontinuity. |  |
| Tomlin (2006); Spiegler et al. (2012); Ivanov et al. (2014a); Turnquist and Vugrin (2013); Sawik (2013); Torabi et al. (2015); Sahebjam- nia et al. (2015); Kamalahmadi and Mellat Parast (2016b); Kamalahmadi and Mella Parast (2017); Khalili et al. (2016); Elluru et al. (2017); Ivanov (2018a); Rezapour et al. (2018); Jabarzadeh et al. (2018); Ivanov et al. (2018); Lücker et al. (2018); Sawki (2018); Tan et al. (2019) |  | Emergency inventory of manufacturer and backup capacity of supplier | Backup capacity and emergency inventory could reduce vulnerability of SC and enhance the SC’s resilience. |  |
| Sawik (2011); Sawik (2013); Sadghiani et al. (2013); Meena and Sarmah (2013); Zhang et al. (2015); Bicer (2015); Torabi et al. (2015); Namdar et al. (2017); Lücker and Seifert (2017) ; Ivanov et al. (2017a,b); Ivanov (2018a) |  | Multiple sourcing strategy | Multiple sourcing strategy has a higher level of as- sociation with SCR as compared with single sourc- ing strategy. |  |
| Hosseini and Barker (2016c); Hosseini et al. (2019) |  | Maintenance and reliability | Manufacturers could improve their resilience by collaborating with reliable suppliers with lower dis- ruption rates. |  |
| Khalili et al. (2016); Kammalahmadi and Mellat Parast (2016b) |  | Multiple transportation channels | Utilizing multiple transportation channels could en- hance the SCR in the case of transportation dam- ages. |  |
|  | Adaptive Capacity |  |  |  |
| Reference |  | Key drivers | Explanation |  |
| Hou et al. (2010); Turnquist and Vugrin (2013); Torabi et al. (2015); Chakraborty et al. (2016); Saghafian and Van Oyen (2016);Hosseini and Barker (2016b); Kama- lahmadi and Mellat Parast (2017); Jabarzadeh et al. (2018) |  | Backup supplier | Utilizing backup supplier when facing a disruption may improve the SCR |  |

---

## 第 41 页

Liu and Lee Lam (2013); Khaled et al. (2015);
Khalili et al. (2016); Hosseini and Barker
(2016b); Hosseini and Khaled (2016e); Wang
et al. (2016)
Rerouting
Freight rerouting particularly in multi-modal trans-
portation systems in the case of damage to trans-
portation mode could enhance the SCR
Wieland and Wallenburg (2013); Scholten
and Scilder (2015); Reyes Levalle and Nof
(2015a,b); Mandal et al. (2016);
Communication
Lack of information sharing, organizations and col-
laboration among SC partners in the case of disrup-
tion could delay recovery process and reduce resili-
ence of SC as whole.
Biringer et al. (2013); Mancheri et al. (2018)
Substitution
Alternative power sources in power plants with
dual fuel capability could enhance the resilience
when the primary fuel supply is disrupted. Substi-
tuting raw materials of manufacturer with an alter-
native choice could reduce the likelihood of SC dis-
ruption.
Restorative Capacity
Reference
Key drivers
Explanation
Turnquist and Vugrin (2013); Sahebjamnia et
al. (2015); Hosseini and Barker (2016b);
Morshedlou et al. (2018)
Budget and resource restoration
SC companies with a higher budget and resource
(man/hour) restoration capability will have a
shorter recovery time from disruption, resulting in
higher resilience achievement.

| Liu and Lee Lam (2013); Khaled et al. (2015); Khalili et al. (2016); Hosseini and Barker (2016b); Hosseini and Khaled (2016e); Wang et al. (2016) |  | Rerouting | Freight rerouting particularly in multi-modal trans- portation systems in the case of damage to trans- portation mode could enhance the SCR |  |
| --- | --- | --- | --- | --- |
| Wieland and Wallenburg (2013); Scholten and Scilder (2015); Reyes Levalle and Nof (2015a,b); Mandal et al. (2016); |  | Communication | Lack of information sharing, organizations and col- laboration among SC partners in the case of disrup- tion could delay recovery process and reduce resili- ence of SC as whole. |  |
| Biringer et al. (2013); Mancheri et al. (2018) |  | Substitution | Alternative power sources in power plants with dual fuel capability could enhance the resilience when the primary fuel supply is disrupted. Substi- tuting raw materials of manufacturer with an alter- native choice could reduce the likelihood of SC dis- ruption. |  |
|  | Restorative Capacity |  |  |  |
| Reference |  | Key drivers | Explanation |  |
| Turnquist and Vugrin (2013); Sahebjamnia et al. (2015); Hosseini and Barker (2016b); Morshedlou et al. (2018) |  | Budget and resource restoration | SC companies with a higher budget and resource (man/hour) restoration capability will have a shorter recovery time from disruption, resulting in higher resilience achievement. |  |

---

## 第 42 页

References
1. Ambulkar, S., J. Blackhurst, S. Grawe (2015). Firm's resilience to supply chain disruptions: Scale develop-
ment and empirical examination. Journal of Operations Management, 33(34), 111–122
2. Amindoust, A. (2018). A resilient-sustainable based supplier selection model using a hybrid intelligent
method. Computers & Industrial Engineering, 126: 122-135.
3. Barker, K., Santos, JR. (2010). Measuring the efficacy of inventory with a dynamic input-output model.
International Journal of Production Economics, 126(1): 130-143.
4. Barroso, A., Machado, H., Cruz-Machado, V. (2011). The resilience paradigm in the supply chain manage-
ment: A case study” Proceedings of the IEEE, 928-932.
5. BBC
News.
2011.
Japan
disaster:
Supply
shortages
in
three
months.
http://www.
bbc.com/news/business-12782566.
6. Behzadi, G., O’Sullivan, M.J., Olsen, T.L., Scrimgeour, F., Zhang, A. (2017). Robust and resilient strategies
for managing supply disruptions in an agribusiness supply chain, International Journal of Production Eco-
nomics, 191, 207-220.
7. Bicer, I. (2015). Dual sourcing under heavy-tailed demand: An extreme value theory approach. International
Journal of Production Research, 53(16), 4979-4992.
8. Biringer, B.E., Vugrin, E.D., Warren, D.E. Critical infrastructure system security and resiliency, CRC Press
Taylor & Francis, 1st editions, 2013.
9. Blackhurst, J., Dunn, J., Craighead, C. (2011). An empirically derived framework of global supply resiliency.
Journal of Business Logistics, 32(4), 347-391.
10. Bllomberg  2011. https://www.bloomberg.com/news/articles/2014-06-12/boeing-hands-21-of-777x-plane-s-
parts-to-japanese-companies
11. Blome, C., Schoenherr, T. and Rexhausen, D. (2013) Antecedents and enablers of supply chain agili-ty and
its effect on performance. International Journal of Production Research, 51 (4), 1295-1318.
12. Bode C, Macdonald JR (2017). Stages of Supply Chain Disruption Response: Direct, Constraining, and Me-
diating Factors for Impact Mitigation. Decision Sciences, 48(5), 836-874.
13. Bonanno, G.A., Galea, S. (2007). What predicts psychological resilience after disaster? The role of de-
mographics, resources and life stress. Journal of Consulting and Clinical Psychology, 75(5), 671-682.
14. Bonanno, G.A., Moskowitz, J.T., Papa, A., Folkman, S. (2005). Resilience to loss in Bereaved Spouses,
Bereaved Parents, and Bereaved Gay Man, Journal of Personality and Social Psychology, 88(5), pp. 827-
843.
15. Brandon-Jones, E., Squire, B., Autry, C.W., Petersen, K.J. (2014). A contingent resource-based perspective
of supply chain resilience and robustness. Journal of Supply Chain Management, 50(3): 55-73.
16. Brusset, X., Teller, C. (2017). Supply chain capabilities, risks, and resilience. International Journal of Pro-
duction Economics, 184: 59-68.
17. Business Continuity Institute, BCI (2013). Supply Chain Resilience Report. http://www.bcifiles.com/bci-
supply-chain-resilience-2015.pdf
18. Cao, M., Vondermbse, M., Zhang, Q, Ragu-Nathan, T.S. (2010). Supply chain collaboration: conceptualiza-
tion and instrument development. International Journal of Production Research, 48(22), 6613-6635.
19. Cardoso, S.R., Barbosa-Povoa, A.P., Relvas, S., Novais, A.Q. (2015). Resilience metrics in the assessment
of complex supply-chains performance operating under demand uncertainty, Omega, 56, 53-73.
20. Carvalho, H., Azevedo, S.G., Cruz-Machado, V. (2012). Agile and resilient approaches to supply chain man-
agement: influence on performance and competitiveness, Logistics Research, 4(1/2), 49-62.
21. Chakraborty, T., Chauhan, S.S., & Ouhimmou, M. (2016). Mitigating Supply Disruption with Backup Sup-
plier under Uncertain Demand : Competition and Cooperation.
22. Chen, C. (2016). CiteSpace: A practical guide for mapping scientific literature (Computer Science, technol-
ogy and Applications). Nova Science Pub Inc; UK edition.
23. Chen, C., Zhang, J., and Vogeley, M.S. (2009). Visual analysis of scientific discoveries and knowledge dif-
fusion.
24. Chen, D., Luo, Z., Webber, M., Chen, J. (2016). Bibliometric and visualized analysis of energy research.
Ecological Engineering, 90, 285-293.
25. Choi TM, Lambert JH. (2017) Advances in risk analysis with big data. Risk Analysis 37, 8, 1435-1442.
26. Choi TM, Chan HK, Yue X. Recent development in big data analytics for business operations and risk man-
agement. IEEE Transactions on Cybernetics (2017) 47, 1, 81-92.

---

## 第 43 页

27. Chopra, S., G. Reinhardt, and U. Mohan. (2007). The importance of decoupling recurrent and disruption risks
in a supply chain. Naval Research Logistics, 54(5): 544–555.
28. Chopra, S., Sodhi, M.S. (2014). Reducing the risk of supply chain disruptions. MIT Sloan Management Re-
view, Spring 2014.
29. Chowdhury, Md. H., Quaddus, M. (2017). Supply chain resilience: conceptualization and scale development
using dynamic capability theory. International Journal of Production Economics, 188: 185-204.
30. Christopher, M., Holweg, M. (2011). Supply chain 2.0: managing SCs in era of turbulence. International
Journal of Physical Distribution & Logistics Management, 41(1): 63-82.
31. Christopher, M., Lee, H. (2004). Mitigating supply chain risk through improved confidence. International
Journal of Physical Distribution & Logistics Management, 34(5), 388-396.
32. Christopher, M., Peck, H. (2004). Building the resilient supply chain. The International Journal of Logistics
Management, 15(2): 1-14.
33. Closs, D., McGarrell, E. (2004). Enhancing security throughout the supply chain. IBM Center for the Busi-
ness of Government, Special Report Series, 1-52. http://www.businessofgovernment.org.
34. Datta, P.P., Christopher, M., Allen, P. (2007). Agent-based modeling of complex production/distribution
systems to improve resilience. International Journal of Logistics Research and Applications, 10, 187-203.
35. Diabat, A., Jabbarzadeh, A., Khosrojerdi, A. (2018). A perishable product supply chain network problem
with reliability and disruption considerations. International Journal of Production Economic, In press.
36. Dixit, V., Seshadrinath, N., Tiwari, M.K. (2016). Performance measures based optimization of supply net-
work resilience: A NSGA-II + Co-kriging approach. Computers & Industrial Engineering, 93: 205-214.
37. Dolgui, A., Ivanov, D., Sokolov, B. (2018). Ripple Effect in the Supply Chain: An Analysis and Re-cent
Literature. International Journal of Production Research, 56(1-2), 414-430.
38. Dubey, R., Altay, N., Gunasekaran, A., Blome, C., Papadopoulos, T., and Childe, S. J. (2018) Supply Chain
Agility, Adaptability and Alignment: Empirical Evidence from the Indian Auto Components Industry. Inter-
national Journal of Operations & Production Management, 38 (1). pp. 129-148.
39. Dubey, R., Gunasekaran, A., Childe, S. J, Papadopoulos, A., Blome, C. and Luo, Z. (2017) Antecedents of
resilient supply chains: an empirical study. IEEE Transactions on Engineering Management, 99, 1-12.
40. Duhadway, S., Carnovale, S., Hazen, B. (2018) Understanding risk management for intentional supply chain
disruptions: risk detection, risk mitigation, and risk recovery. Annals of Operations Research, 1-20.
41. Elluru, S., Gupta, H., Karu, H., Prakash Singh, S. (2017). Proactive and reactive models for disaster resilient
supply chain. Annals of Operations Research, 1-26.
42. Ergun, A., Heier Stamm, J.L., Keskinocak, P., Swann, J.L. (2010). Waffle house restaurants hurricane re-
sponse: a case study. International Journal of Production Economics, 126(1): 111-120.
43. Erol, O., Sauser, B., Mansouri, M. (2010). A framework for investigation into extended enterprise resilience.
Enterprise Information Systems, 4(2), 111-136.
44. Fahimnia, B., Jabarzadeh, A. (2016). Marrying supply chain sustainability and resilience: A match made in
heaven. Transportation Research-Part E, 91: 306-324.
45. Fahimnia, B., Sarkis, J., Davarzani, H. (2015b). Green supply chain management: A review and bibliometric
analysis. International Journal of Production Economics, 162, 101-114.
46. Fahimnia, B., Tang, C.S., Davarzani, H., Sarkis, J. (2015a). Quantitative models for managing supply chain
risks: A review. European Journal of Operational Research, 247: 1-15.
47. Fahimnia, B., Jabarzadeh, A., Sarkis, J. (2018). Greening versus resilience: A supply chain design perspec-
tive. Transportation Research- Part E, 119, 129-148.
48. Faisal, M.N. (2010). Sustainable SCs: a study of interaction among the enablers. Business Process Manage-
ment Journal, 16(3): 508-529.
49. Falasca, M., Zobel, C., Cook. D. (2008). A decision support framework to assess supply chain resilience.
Proceeding of the 5th International ISCRAM Conference, edited by F. Fiedrich, and B. Van de Walle, 596-
605, Washington, DC, USA.
50. Fiksel, J. (2003). Designing resilient, sustainable systems. Environmental Science and Technology, 37 (23):
5330-5339.
51. Francis, V. (2008). Supply chain visibility: lost in translation?, Supply Chain Management: An International
Journal, 13 (3): 180-184.
52. Gaonkar, R., Viswanadham, N. (2007). Analytical framework for the management of risk in SCs. IEEE
Transactions on Automation Science and Engineering, 4(2): 265-273.
53. Garcia-Herreros, P., Wassick, J.M., Grossmann, I.E. (2014). Design of resilient supply chains with risk of
facility disruptions. Industrial & Engineering Chemistry Research, 53(44), 17240-17251.

---

## 第 44 页

54. Garvey, M.D., Carnovale, S., Yeniyurt, S. (2015). An analytical framework for supply network risk propa-
gation: A Bayesian network approach. European Journal of Operational Research, 243 (2): 618-627.
55. Govindan, G., A. Jafarian, M. E. Azbari, T.M. Choi. (2016). Optimal Bi-Objective Redundancy Allocation
for Systems Reliability and Risk Management. IEEE Transactions on Cybernetics, 46, 1735-1748.
56. Guoping, C., Xinqiu, Z. (2010). Research on supply chain resilience evaluation. Proceedings of the 7th Inter-
national Conference on Innovation & Management, 1558-1562.
57. Gupta V., He B., Sethi S.P. (2015). Contingent sourcing under supply disruption and competition. Interna-
tional Journal of Production Research, 53(10), 3006-3027.
58. Hartvisgen, G., Kinzig, A., Peterson, G. (1998). Complex adaptive systems: Use and analysis of complex
adaptive systems in ecosystem science: overview of special section, EcoSystems, 1(5), 427-430.
59. Hasani, A., Khosrojerdi, A. (2016). Robust global supply chain network design under disruption and uncer-
tainty considering resilience strategies: A parallel memetic algorithm for a real-life case study. Transporta-
tion Research Part E, 87: 20-52.
60. HBS (2017). Will Typhoons in Southeast Asia Stop You from Staying Hydrated This Summer?
https://rctom.hbs.org/submission/will-typhoons-in-southeast-asia-stop-you-from-staying-hydrated-this-
summer/, accessed on January 5, 2018.
61. He, J, F Alavifard, D Ivanov, Jahani H. (2018). A real-option approach to mitigate disruption risk in the
supply
chain.
Omega:
The
International
Journal
of
Management
Science,
https://doi.org/10.1016/j.omega.2018.08.008.
62. Ho, W., Xu, X., Dey, P.K. (2010). Multi-criteria decision making approaches for supplier evaluation and
selection: a literature review. European Journal of Operational Research, 202: 16-24.
63. Ho, W., T. Zheng, H. Yildiz & S. Talluri (2015) Supply chain risk management: a literature review. Interna-
tional Journal of Production Research, 53(16), 5031-5069.
64. Hohenstein, N-O., Feisel, E., Hartman, E., Giunipero, L. (2015). Research on the phenomenon of supply
chain resilience: a systematic review and paths for future investigation. International Journal of Physical
Distribution & Logistics Management, 45(12), 90-117.
65. Hollnagel, E. (2006). Achieving system safety by resilience engineering. The 1st IET International Confer-
ence on System Safety, June 6-8, London, UK, 184-195.
66. Hosseini, S., Barker, K. (2016b). A Bayesian network model for resilience-based supplier selection. Interna-
tional Journal of Production Economics, 180, 68-87.
67. Hosseini, S., Barker, K. (2016c). Modeling infrastructure resilience using Bayesian networks: a case study
of Inland waterway ports. Computers & Industrial Engineering, 93, 252-266.
68. Hosseini, S., Barker, K., Ramirez-Marquez, JE. (2016a). A review of definitions and measure of system
resilience. Reliability Engineering and System Safety, 145, 47-61.
69. Hosseini, S., Khaled, A. (2016). A hybrid ensemble AHP approach for resilient supplier selection. Journal
of Intelligent Manufacturing, 1-22.
70. Hosseini, S., Khaled, A., Sarder, MD. (2016d). A general framework for assessing system resilience using
Bayesian networks: A case study of sulfuric acid manufacturer. Journal of Manufacturing Systems, 41, 211-
227.
71. Hosseini, S., Morshedlou, N., Barker, K., Sarder, MD. (2018). Resilient supplier selection and optimal order
allocation under disruption risks. In revisions at International Journal of Production Economics.
72. Huffington
Post,
2015.
Toyota
among
Japanese
automaker
extending
plant
closures.
http://www.huffingtonpost.com/2011/03/16/japans-auto-plant-closures_n_
836653.html
73. Ivanov D. (2017a) Simulation-based ripple effect modelling in the supply chain. International Journal of
Production Research, 55(7), 2083-2101.
74. Ivanov D. (2017b). Simulation-based single vs dual sourcing analysis in the supply chain with con-sideration
of capacity disruptions, Big Data and demand patterns. International Journal of Integrated Supply Manage-
ment, 11(1), 24-43.
75. Ivanov D. (2018a). Revealing interfaces of supply chain resilience and sustainability: a simulation study.
International Journal of Production Research, 56(10), 3507-3523.
76. Ivanov D., Das, A., Choi T.-M. (2018). Special Issue on New Flexibility Drivers in Manufacturing, Service,
and Supply Chain Systems, International Journal of Production Research, 56(10).
77. Ivanov D., Pavlov A., Pavlov D., Sokolov B. (2017a). Minimization of disruption-related return flows in the
supply chain, International Journal of Production Economics, 183, 503-513.

---

## 第 45 页

78. Ivanov D., Rozhkov M. (2017). Coordination of production and ordering policies under capacity disruption
and product write-off risk: An analytical study with real-data based simulations of a fast moving consumer
goods company. Annals of Operations Research, published online.
79. Ivanov D., Sokolov, B., & Pavlov, A. (2014b). Optimal distribution (re)planning in a centralized multi-stage
network under conditions of ripple effect and structure dynamics. European Journal of Operational Re-
search, 237(2), 758–770.
80. Ivanov, D. (2018a). Revealing interfaces of supply chain resilience and sustainability: a simulation study.
International Journal of Production Research, 56 (10): 3507-3523.
81. Ivanov, D. (2018b). Structural Dynamics and Resilience in Supply Chain Risk Management. Springer, New
York.
82. Ivanov, D., B. Sokolov (2013) Control and system-theoretic identification of the supply chain dynamics do-
main for planning, analysis, and adaptation of performance under uncertainty, European Journal of Opera-
tional Research, 224(2), 313–323.
83. Ivanov, D., B. Sokolov, A. Pavlov, A. Dolgui, D. Pavlov, (2016) Disruption-driven supply chain (re)-plan-
ning and performance impact assessment with consideration of pro-active and recovery policies, Transpor-
tation Research: Part E, 90, 7-24
84. Ivanov, D., Dolgui A., Sokolov B., Ivanova M. (2017b). Literature review on disruption recovery in the
supply chain. International Journal of Production Research, 55(20), 6158-6174.
85. Ivanov, D., Dolgui, A., Sokolov, B. (2018b). The impact of digital technology and Industry 4.0 on ripple
effect and supply chain risk analytics. International Journal of Production Research,
https://doi.org/10.1080/00207543.2018.1488086
86. Ivanov, D., Dolgui, A., Sokolov, B., Werner, F., Ivanova, M. (2016). A dynamic model and an algorithm for
short-term supply chain scheduling in the smart factory industry 4.0. International Journal of Production
Research, 54 (2): 386-402.
87. Ivanov D., Dolgui, A. (2019) Low-Certainty-Need (LCN) Supply Chains: A new perspective in managing
disruption risks and resilience. International Journal of Production Research, in press.
88. Ivanov, D., Sokolov, B., Dolgui, A. (2014a). The ripple effect in SCs: trade-off ‘efficiency-flexibility-resili-
ence’s in disruption management, International Journal of Production Research, 52 (7): 2154-2172.
89. Jabarzadeh, A., Fahimnia, B., Sabouhi, F. (2018). Resilient and sustainable supply chain design: sustainabil-
ity analysis under disruption risks, International Journal of Production Research.
90. Jain, V., Benyoucef, L. Deshmukh, S.G. (2008). A new approach for evaluating agility in SCs using fuzzy
association rules mining. Engineering Applications of Artificial Intelligence, 46(23), 367-385.
91. Juttner, U., Maklan, S. (2011). Supply chain resilience in the global financial crisis: an empirical study. Sup-
ply Chain Management, 16(4), 246-259.
92. Käki, A., Salo, A., Talluri, S. (2015). Disruptions in supply networks: A probabilistic risk assessment ap-
proach. Journal of Business Logistics, 36(3): 273-287.
93. Kamalahmadi, M., Mellat Parast, M. (2016). A review of the literature on the principles of enterprise and
supply chain resilience: Major findings and directions for future research. International Journal of Produc-
tion Economics, 171: 116-133.
94. Kamalahmadi, M., Mellat Parast, M. (2017). An assessment of supply chain disruption mitigation strategies.
International Journal of Production Economics, 184: 210-230.
95. Kamalahmadi, M., Mellat-Parast, M. (2015b). Developing a resilient supply chain through supplier flexibility
and reliability assessment. International Journal of Production Research, 302-321.
96. Kerkhoff, A.J., Enquist, B.J. (2007). The implications of scaling approaches for understanding resileince and
reorganization in ecosystems, BioScience 57(6), 489-499.
97. Khaled, A.A., Jin, M., Clarke, D.B., Hoque, M.A. (2015). Train design and routing optimization for evaluat-
ing criticality of freight railroad infrastructures. Transportation Research Part B, 71: 71-84.
98. Khalili, S.M., Jolai, F., Torabi, S.A. (2016). Integrated production-disruption planning in two-echelon sys-
tems: a resilience view. International Journal of Production Research, 55(4), 2017.
99. Kim, Y., Chen, Y., Linderman, K. (2015). Supply network distribution and resilience: a network structural
perspective. Journal of Operations Management, 33: 43-59.
100. Kull, T.J., Talluri, S. (2008). A supply risk reduction model using integrated multi-criteria decision making.
IEEE Transactions on Engineering Management, 55(3): 409-419.
101. Li, H., Pedrielli, G., Lee, L.H., Chew, E.P. (2017a). Enhancement of supply chain resilience through inter-
echelon information sharing. Flexible Services and Manufacturing, 29(2), 260-285.

---

## 第 46 页

102. Li, X., Ma, E., Qu, H., Davis, W.E. (2017b). Knowledge mapping of hospitality research-A visual analysis
using CiteSpace. International Journal of Hospitality Management, 60, 77-93.
103. Lima-junior, F.R., Carpinetti, L.C.R. (2016). A multicriteria approach based on fuzzy QFD for choosing
criteria for supplier selection. Computers & Industrial Engineering, 101: 269-285.
104. Liu, C-L., Shang, K-C., Lirn, T-C., Lai, K-H., Venus Lun, Y.H. (2018). Supply chain resilience, firm perfor-
mance, and management policies in the liner shipping industry. Transportation Research Part A: Policy and
Practice, 110: 202-219.
105. Liu, T., Lee Lam. (2013). Impact of port disruption on transportation network.
106. Longo, F., Oren, T. (2008). Supply chain vulnerability and resilience: A case study of the art overview.
Proceedings of European Modeling & Simulation Symposium, edited by Campora S. Giovani, September
17-19, Italy.
107. LST Commercial Credit, (2014), https://www.1stcommercialcredit.com/blog/category/distribution/creat-
ing-a-resilient-supply-chain/
108. Lücker, F., Seifert, R.W. (2017). Building up resilience in a pharmaceutical supply chain through inventory,
dual sourcing and agility capacity. Omega, 73: 114-124.
109. Lücker F., R. W. Seifert & I. Biçer (2018) Roles of inventory and reserve capacity in mitigating supply chain
disruption risk, International Journal of Production Research, DOI: 10.1080/00207543.2018.1504173
110. Luxburg, U.v. (2006). A tutorial on spectral clustering. Max Plank Institute for Biological Cybernetics.
111. Mancheri, N.A., Sprecher, B., Deetman, S., Young, S. B., Bleischwitz, R., Dong, L., Kleijn, R., Tukker, A.
(2018). Resilience in the tantalum supply chain. Resources, Conservation & Recycling, 129: 56-69.
112. Mandal S., Sarathy, R., Rao Korasiga V., Bhattacharya S., Ghosh Dastidar, S (2016). International Journal
of Disaster Resilience in the Built Environment, 7 (5): 544-562
113. Mandal, S. Supply chain resilience: a state-of-art review and research directions. International Journal of
Disaster Resilience in the Built Environment, 5(4): 427-453.
114. Margolis, J.T., Sullivan, K.M., Mason, S.J., Maganotti, M. (2018). A multi-objective optimization model for
designing resilient supply chain networks. International Journal of Production Economics, 204: 174-185.
115. Meena, P., Sarmah, S. (2013). Multiple sourcing under supplier failure risk and quantity discount: A genetic
algorithm approach. Transportation Research Part E: Logistics and Transportation Review, 50: 84-97.
116. Millar, M. (2015). Global Supply Chain Ecosystems, Strategic for competitive advantage in a complex, con-
nected world. CPI Group (UK), Ltd. 1st Edition.
117. Mogre, R., Talluri, S., D’Amico, F. (2016). A decision framework to mitigate supply chain risks: an appli-
cation in the offshore-wind industry. IEEE Transactions on Engineering Management, 63(3): 316-325.
118. Mohammed, A., Harris, I., Soroka, A., Nujoom, R. (2018). A hybrid MCDM-fuzzy multi-objective program-
ming approach for a G-resilient supply network design. Computers & Industrial Engineering, In Press.
119. Morshedlou, N., Gonzalez, A.D., Barker, K. (2018). Work crew routing problem for infrastructure network
restoration. Transportation Research Part B, 118, 66-89.
120. Mizgier, K.J., Pasia, J.M. Talluri, S. (2017). Multiobjective capital allocation for supplier development under
risk. International Journal of Production Research, 55(18): 5243-5258.
121. Namdra, J., Sawhney, R., Pradhan, N. (2017). Supply chain resilience for single and multiple sourcing in the
presence of disruption risks. International Journal of Production Research, 1-22.
122. Ni, N., Howell, B.J., Sharkey, T.C. (2018). Modeling the impact of unmet demand in supply chain resiliency
planning, Omega, 86, 1-16.
123. Ouhimmou, Mustapha & Chakraborty, Tulika & Singh Chauhan, Satyaveer. (2016). Mitigating supply dis-
ruption with backup supplier under uncertain demand: competition and cooperation.
124. Pereira, J., Takahashi, K., Ahumada, L., Paredas, F. (2009). Flexibility dimensions to control the bullwhip
effect in a supply chain. International Journal of Production Research, 47(22): 6357-6374.
125. Pettit, J., Croxton, K., Fiksel, J. (2013). Ensuring supply chain resilience: development and implementation
of an assessment tool. Journal of Business Logistics, 34(1): 46-76.
126. Pettit, Timothy, J., Fiksel, J., Croxton, K. (2010). Ensuring supply chain resilience: development of a con-
ceptual frame work. Journal of Business Logistics, 31(1): 1-21.
127. Pires Riberio, H., Barbosa_Povoa, A. (2018). Supply chain resilience: definitions and quantitative modeling
approaches- A literature review. Computers & Industrial Engineering, 115: 109-122.
128. Poins, S., Koronis, E. (2012). Supply chain resilience: definition of concept and its formative elements. Jour-
nal of Applied Business Research 28(5): 921-930.
129. Ponomarov, S., Holcomb. (2009). Understanding the concept of supply chain resilience. The International
Journal of Logistics management, 20(1): 124-143.

---

## 第 47 页

130. Ponomarov. S. (2012). Antecedents and consequences of supply chain resilience: a dynamic capabilities per-
spective. PhD dissertation University of Tennessee-USA.
131. Pramanik, D., Haldar, A., Chandra Mondal, S., Kumar Naskar, S., Ray, A. (2017). Resilient supplier selection
using AHP-TOPSIS-QFD under a fuzzy environment. International Journal of Management Science and
Engineering Management, 12 (1): 45-54.
132. Pregenzer, A. (2011). Systems resilience: a new analytical framework for nuclear nonproliferation. Albu-
querque, MN: Sandia National Laboratories.
133. PWC and the MIT Forum for supply chain innovation. Making the right risk decisions to strengthen opera-
tions performance, 2013. http://pwc.to/2p7kok4
134. Qazi A., Dickson, A., Gaudenzi, B. (2018). Supply chain risk network management: A Bayesian belief net-
work and expected utility based approach for managing supply chain risks. International Journal of Produc-
tion Economics, 196, 24-42.
135. Qazi, A., Quigley, J., Disckson, A., Ekici, S.Q. (2017). Exploring dependency based probabilistic supply
chain risk measures for prioritizing interdependent risks and strategies. European Journal of Operational
Research, 259 (1): 189-204.
136. Ojha, R., Ghadge, A., Kumar Tiwari, M., Bititci, U.S. (2018). Bayesian network modeling for supply chain
risk propagation. International Journal of Production Research, 56(17): 1-25.
137. Reuters 2011. http://www.reuters.com/article/us-japan-supplychain-idUSTRE72M21J20110323
138. Reyes Levalle, R., Nof, S.Y. (2015a). A resilience by teaming framework for collaborative supply networks.
Computers & Industrial Engineering, 90: 67-85.
139. Reyes Levalle, R., Nof, S.Y. (2015b). Resilience by teaming in supply network formation and re-configura-
tion. International Journal of Production Economics, 160: 80-93.
140. Rezapour, S., Naderi, N., Morshedlou, N., Rezapourbenhagh, S. (2018). Optimal deployment of emergency
resources in sudden onset disasters. International Journal of Production Economics, 24, 365-382.
141. Roberta Peria, C., Christopher, M., Da Silva, A.L. (2014). Achieving supply chain resilience: the role of
procurement. Supply Chain Management: An International Journal, 626-642.
142. Rice, J., Caniato, F. (2003). Building a secure and resilient supply network, Supply Chain Management Re-
view, 7(5): 22-30.
143. Rose, A. (2007). Economic resilience to natural and man-made disaster: multidisciplinary origins and con-
textual dimensions. Environmental Hazards, 7(4), 383-398.
144. Sadghiani, N.S., Torabi, S., Sahebjamnia, N. (2015). Retail supply chain network design under operational
and disruption risks. Transportation Research Part E: Logistics and Transportation Review, 75: 95-114.
145. Saenz, J., Revilla, E. (2014). Creating more resilient SCs. MIT Sloan Management Review Summer 2014:
22-24.
146. Sabouhi, F., Pishvaee, S., Jabalameli, M.S. (2018). Resilient supply chain design under operational and dis-
ruption risks considering quality discount: A case study of pharmaceutical supply chain. Computers & In-
dustrial Engineering, 126, 657-672.
147. Saghafian, S., Oyen, M.P.V. (2012). The value of flexible backup suppliers and disruption risk information:
newsvendor analysis with resource. IIE Transactions, 44(10): 834-867.
148. Saghafian, S., Van Oyen, M.P. (2016). Compensating for dynamic supply disruptions: backup flexibility
design. Operations Research; 64(2) 390-405.
149. Sahebjamnia, N., Torabi, A., Mansouri, A. (2018). Building organizational resilience in the face of multiple
disruptions. International Journal of Production Economics, 197: 63-83.
150. Sahebjamnia, N., Torabi, S.A., Mansouri, S.A. (2015). Integrated business continuity and disaster recovery
planning: toward organizational resilience. European Journal of Operational Research, 242 (1): 261-273.
151. Saunders, M., Lewis, P., Thornhill, A. (2009). Research methods for business students. Harlow: Pearson.
152. Sawik, T. (2011). Selection of supply portfolio under disruption risks. Omega, 39 (2): 194-208.
153. Sawik, T. (2013). Selection and protection of suppliers in a supply chain with disruption risks. International
Journal of Logistics Systems and Management, 15: 143-159.
154. Sawik, T. (2018). Two-period vs. multi-period model for supply chain disruption management. International
Journal of Production Research, https://doi.101080/00207543.2018.1504246
155. Scholten, K., Schilder, S. (2015). The role of collaboration in supply chain resilience. Supply Chain Man-
agement: An International Journal, 20(4): 471-484.
156. Sheffi, Y., Rice, J.B. Jr. (2005). A supply chain view of the resilient enterprise. MIT Sloan Management
Review, 47(1), 41-48.

---

## 第 48 页

157. Shi, J., and Malik, J. (2000). Normalized cuts and image segmentation. IEEE Transactions on Pattern Anal-
ysis and Machine Intelligence, 22(8), 888-905.
158. Shrivastava, H., Dutta, P., Krishamoorthy, M., Suyawanshi, P. Proceedings of the International MultiCon-
ference Engineers and Computer Scientists 2017, Vol II, IMECS 2017, March 15-17, Hong Kong.
159. Snyder, L. V., Z. Atan, P. Peng, Y. Rong, A. Schmitt, and B. Sinsoysal, 2016. OR/MS models for supply
chain disruptions: A review, IIE Transactions, 48(2), 89-109.
160. Soni, U., Jain, V., Kumar, S. (2014). Measuring supply chain resilience using a deterministic modeling ap-
proach. Computers & Industrial Engineering, 74: 11-25.
161. Spiegler, V.L.M., Niam, M.M., Wikner, J. (2012). A control engineering approach to the assessment of sup-
ply chain resilience. International Journal of Production Research, 50(21): 6162-6187.
162. Tang, C. (2006a). Perspectives in supply chain risk management. International Journal of Production Eco-
nomics, 103(2): 451-488.
163. Tang, C. (2006b). Robust strategies for mitigating supply chain disruptions. International Journal of Logis-
tics, 9(1): 33-45.
164. Tomlin, B. T. (2006). On the value of mitigation and contingency strategies for man- aging supply chain
disruption risks. Management Science, 52 (5), 639–657.
165. Torabi, S.A., Baghersad, M., Mansouri, S.A. (2015). Resilient supplier selection and order allocation under
operational and disruption risks. Transportation Research – Part E, 79: 22-48.
166. Tukamuhabwa, B.R., Stevenson, M., Busby, J., Zorzini, M. (2015). Supply chain resilience:  definitions,
review and theoretical foundations for future study. International Journal of Production Research, 53(18),
5592-5623.
167. Turnquist, M., Vugrin, E. (2013). Design for resilience in infrastructure distribution networks. Environment
Systems & Decisions, 33(1), 104-120.
168. Van der Vorst JVD, Beulens A. (2002). Identifying sources of uncertainty to generate supply chain redesign
and strategies. International Journal of Physical Distribution & Logistics Management, 32(6): 409-430.
169. Verma, S., Jain, V., Majumdar, A. (2011). Modeling and agile supply chain: research challenges and future
directions: Proceedings of the International Conference on Soft Computing for Problem Solving, Dec. pp.
277-285.
170. Wang, X., Herty, M., Zhao, L. (2016). Contingent rerouting for enhancing supply chain resilience from sup-
plier behavior perspective. International Transactions in Operational Research, 23: 775-796.
171. Wang, J., Dou, R., Muddada, R.R., Zhang, W. (2018). Management of a holistic supply chain network for
proactive resilience: Theory and case study. Computers & Industrial Engineering, 125, 668-677.
172. Webb, C.T. (2007). What is the role of ecology in understanding ecosystem resilience. BioScience, 57(6),
470-471.
173. Wieland, A., Marcus Wallenburg, C. (2013). The influence of rational competencies on supply chain resili-
ence: a relational view. International Journal of Physical Distribution & Logistics Management, 43(4): 300-
320.
174. Xiang, C., Wang, Y., Liu, H. (2017). A scientometrics review on nonpoint source pollution research. Eco-
logical Engineering, 99, 400-408.
175. Yang, T., Fan, W. (2016). Information management strategies and supply chain performance under demand
disruptions. International Journal of Production Research, 54(1): 8-27.
176. Yang, Z., Aydin, G., Babich, V. , & Beil, D. R. (2009). Supply disruptions, asymmetric information, and a
backup production option. Management Science, 55 (2), 192–20.
177. Yildiz H., J. Yoon, S. Talluri and W. Ho (2016). Reliable Supply Chain Network Design. Decision Sciences,
47(4), 661–698.
178. Yu, D., Xu, C. (2017). Mapping research and carbon emissions trading: a co-citation analysis. Renewable
and Sustainable Energy Reviews, 74, 1314-1322.
179. Yoon, J., Yildiz, H., Talluri, S. (2016). Risk management strategies in transportation capacity decisions: an
analytical approach. Journal of Business Logistics, 37(4): 364-381.
180. Yoon, J., S. Talluri, H. Yildiz, W Ho (2018). Models for Supplier Selection and Risk Mitigation: A Holistic
Approach. International Journal of Production Research, 56(10), 3636-3661.
181. Zhang, Y., Qi, M., Lin, W-H., Miao, L. (2015). A metaheuristic approach to the reliable location routing
problem under disruption. Transportation Research Part E: Logistics and Transportation Review, 83: 90-
110.

---
