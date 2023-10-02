# Blue Team introduction

* Type : Solo
* Duration : 5 days (intro)

## Prerequisites

* Operating Systems ([01-Linux](../01-Linux/), [02-Windows](../02-Windows/))
* Basic understanding of Networking ([00-Network](../00-Network/))
* TCP/IP model ([TCP/IP basic](https://openclassrooms.com/fr/courses/6944606-concevez-votre-reseau-tcp-ip), [TCP/IP advanced](https://openclassrooms.com/fr/courses/2340511-maitrisez-vos-applications-et-reseaux-tcp-ip))

## Learning objectives

* Monitor and investigate the alerts
* Configure and manage the security tools
* Develop and implement basic IDS

## Overview

The blue team track will be in 2 phases, although some of you will have the opportunity to specialize in specific niches, the majority of those who will consider working on the blue team side will have to go through monitoring, at different levels, with different tools, with other tasks at the same time, sometimes only that, in some cases, there will be incident response to fix the problem, sometimes it will just be escalating the problem to other teams, in other cases it will depend on the protocols and the strategy of your company and I think you see where I'm going with this, it's very difficult to standardize an environment similar to what you're going to encounter in your internship or even at the beginning of your career.

At first, the various introductory modules will give you a first approach and will allow you to acquire the essential knowledge for a good understanding of the context, of the tools used and of their utilities.

The second phase, the most interesting one, will make the link with the period of the "Summer-Pastures" and the preparation of the internship and it will be up to you to manage your roadmap and thus your planning, you will find still add-ons in the module "Summer-Pastures", an index for the various tools (Wireshark, Splunk, Snort, Suricata, Wazuh), training labs, complementary modules, rooms with a specific subject like malware analysis, forensics, Threat Hunting, SOC assessments, Mitre emulation...

## Intro

### Contextual setting

*What is an SOC (Security Operations Center) ? The job of a SOC is to investigate, monitor, prevent and respond to threats and protect information systems, personnel data and corporate integrity.*

*Generally speaking, there are three levels of intervention: prevention, investigation and response.*

![](https://www.exabeam.com/wp-content/uploads/BLOG-SOC-Team-Roles-and-Responsibilities-Explained-inpage-01.jpg)

**Prevention**: *The first phase is to detect and hunt for threats, to work on a security roadmap to protect the organization and to be prepared for the different scenarios.*
*Prevention methods include gathering intelligence on the latest threats, threat actors and their TTPs (tactics, techniques and procedures). They also include maintenance procedures such as updating firewall signatures, fixing vulnerabilities in existing systems, establishing block lists and security lists of applications, email addresses and IP addresses.*

**Investigation**: *This is monitoring, using SIEM (Security Information and Event Management) and EDR (Endpoint Detection and Response) tools to monitor suspicious activity and prioritize alerts based on their level (Low, Medium, High and Critical)*

**Response**: *Once the investigation is complete, the SOC must coordinate and take action by isolating compromised hosts, terminating ongoing malicious processes and ensuring the incident does not reoccur.*

As an introduction, I propose you to review the main lines of defensive security and the scope of a Junior security analyst, you will also find the NDE (Network defense essential) of the Eccouncil (if you wish *) which summarizes the fundamentals of computer security, the protocols, the concepts, the frameworks, the controls, the categories of tools and which gives you a first approach of the topic

- [Defensive security](https://tryhackme.com/room/defensivesecurity)

- [Junior analyst](https://tryhackme.com/room/jrsecanalystintrouxo)

- *[Network defense essentials](https://codered.eccouncil.org/courseVideo/network-defense-essentials?logged=true)

* Frameworks
    - [Pyramid of pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)

    - [Intro Mitre](https://tryhackme.com/room/mitre)

    - [Mitre doc](https://attack.mitre.org/resources/getting-started/)

### Threat intelligence

What is threat intelligence?
It is the process of sifting through data, examining it in context to identify and better understand threats, with the primary goals of preventing data loss, providing guidance on security measures and sharing observed strategies, and creating a collective foundation to fight cybercrime.

- [Tactics-tech-process](https://www.optiv.com/explore-optiv-insights/blog/tactics-techniques-and-procedures-ttps-within-cyber-threat-intelligence)

- [Threat intelligence](https://tryhackme.com/room/cyberthreatintel)

### Fundamentals of endpoint security

Endpoint security is the practice of securing endpoints or entry points to end-user devices, such as desktops, laptops, and mobile devices, to prevent them from being exploited by "des malfrats"

- [Endpoint sec](https://tryhackme.com/room/introtoendpointsecurity)

### Lifecycle

Incident response is the process by which an organization responds to cyber threats such as cyber attacks, security breaches and server outages. In this section, we will cover some basic concepts of DFIR, the incident response processes used in the industry, and some of the tools used.

- [Incident response fundamentals](https://app.cybrary.it/browse/course/incident-response-lifecycle)
- [Intro DFIR](https://tryhackme.com/room/introductoryroomdfirmodule)

## Practice

### Secure your infrastructure

In this room, we will focus on the steps to follow to secure your information system, secure the architecture, filter the network, secure it with OpenSSH, secure Active directory, secure windows/linux and other important points

- *[Check infra](https://openclassrooms.com/fr/courses/1761876-securisez-vos-infrastructures)

### OS

In this part we will perform the basic audit of an operating system, the boot process, the system, the services, the network access

- *[Basic audit OS](https://openclassrooms.com/fr/courses/2035746-auditez-la-securite-dun-systeme-dexploitation)

### Traffic analysis

Well, a lot of blabla, it's time to focus on the tools

* SNORT is an open-source Network Intrusion Detection and Prevention System (NIDS/NIPS). This IPS uses a set of rules that help identify malicious activity and generate alerts for users.
    - Intro (video) : [Intro IDS](https://youtu.be/ClXsXsleof4) ,[Intro Snort](https://www.youtube.com/watch?v=8lOTUqfkAhQ), [Setting](https://youtu.be/U6xMp-MIEfA), [IDS with Snort](https://youtu.be/Gh0sweT-G30)
    - [Snort basics](https://tryhackme.com/room/snort)
    - [Snort challenge](https://tryhackme.com/room/snortchallenges2)
    - [Snort doc](https://www.snort.org/documents)

* Wireshark is an open-source network packet analysis tool used to sniff and examine live traffic and inspect packet captures (PCAP).
    - Intro (video) : [Intro](https://youtu.be/OjQ0gncwS7I), [Setting](https://youtu.be/NwY57Wv0yfA), [Filters](https://youtu.be/-y_ObCrHB0g), [Https Traffic](https://youtu.be/a9eVf2uleaA)
    - [Wireshark basics](https://tryhackme.com/room/wiresharkthebasics)
    - [Wireshark challenge](https://tryhackme.com/room/c2carnage)
    - [Wireshark doc](https://www.wireshark.org/docs/)

### SIEM

SIEM stands for Security Information & Event Management, and is a solution that combines existing tools; namely SIM (Security Information Management) and SEM (Security Event Management). They provide a complete and centralized view of the security of an IT infrastructure.

- [SIEM intro](https://tryhackme.com/room/introtosiem)

- [SIEM monitoring](https://openclassrooms.com/fr/courses/1750566-optimisez-la-securite-informatique-grace-au-monitoring)

### Splunk

Splunk is a software platform for searching, analyzing and visualizing machine-generated data collected from websites, applications, sensors, and devices of all kinds. Simply upload the data to the platform and let Splunk take care of processing it and turning it into actionable information.

Splunk Free is a limited version of Splunk Enterprise that allows you to practice. You can ingest up to 500 MB of data per day, if you exceed this quota, you will have to switch to the enterprise version.
The free license does not expire, however, after the trial version, you may be limited in some features, I slip you 3 open-source alternatives available to take a look ;)

**Learning Objectives** : Collect data, filter according to rules, generate report
**Alternatives** : [OSSIM](https://cybersecurity.att.com/products/ossim), [ELK Stack](https://www.elastic.co/fr/what-is/elk-stack), ...

#### The beginning

- Download : [Splunk entreprise 9.0.2](https://www.splunk.com/en_us/download/splunk-enterprise.html)

- Video:
    - [Intro](https://youtu.be/axHsJBEeqPs), [Setting](https://youtu.be/I98pF5__-_g), [Logs](https://youtu.be/z454piFK8W4)
    - [Splunk getting started](https://www.splunk.com/en_us/download/splunk-enterprise/thank-you-enterprise.html)

- [Splunk free courses](https://www.splunk.com/en_us/training/course-catalog.html?sort=Newest&filters=filterGroup1FreeCourses)

- [Splunk Education](https://education.splunk.com/catalog?category=splunk-courses)

- [Essential guide](https://www.splunk.com/en_us/pdfs/gated/ebooks/the-essential-guide-to-data.pdf)

- [Doc](https://docs.splunk.com/Documentation/Splunk)

#### Try

*Easy*

- [Splunk Search Tuto](https://docs.splunk.com/Documentation/Splunk/latest/SearchTutorial/WelcometotheSearchTutorial?_gl=1*4gs4hi*_ga*NjYwNDk5NTg5LjE2NjM4NTI1MDY.*_ga_5EPM2P39FV*MTY2OTAyODc3NC4xMC4xLjE2NjkwMzAxMDEuNTUuMC4w&_ga=2.140278515.1952817449.1669023005-660499589.1663852506&_gac=1.156718665.1669023087.Cj0KCQiA4OybBhCzARIsAIcfn9kz9FN2zAjfeE6FH5_hIxmkF18ixT4XZpMnpHEYD0h1yZwwrn_dKxUaAiSyEALw_wcB)

*Medium*

- [Splunk Challenge Conti](https://tryhackme.com/room/contiransomwarehgh)
- [Splunk Challenge Eclipse](https://tryhackme.com/room/posheclipse)

### Next ?

This course was just an introduction of course and you will have to work on the automatisms and continue to train. To do this, it's no longer a secret, you need to practice, you will find below links to training rooms available to train your skills apart from those you already know (THM, HTB...)
You will also find a link to the pasture folder, which will contain as mentioned in the overview, a set of additional or specific topics, as well as links to work on other tools related to the needs of your internship and/or with the market standards

* Need for challenges :
    - [Blue Team Labs](https://blueteamlabs.online/home/challenges)
    - [Cyber defenders](https://cyberdefenders.org/blueteam-ctf-challenges/)

* [Summer-pastures : Blue Team (coming soon)](...)

![](https://media.giphy.com/media/l46Cgwa9YZNNrEQla/giphy.gif)

## Resources

- [Attack modeling](https://medium.com/cyberthreatintel/mitre-att-ck-le-nouveau-standard-de-mod%C3%A9lisation-des-attaques-informatiques-9ad37aaec185)

- [Identify web attack](https://app.cybrary.it/browse/course/identifying-web-attacks-through-logs)

- [Mitre repo](https://car.mitre.org/)

- [Mitre ebook](https://www.mitre.org/sites/default/files/2021-11/getting-started-with-attack-october-2019.pdf)

- [Security and compliance](https://logz.io/blog/audit-logs-security-compliance/)

- [Security-awareness](https://www.trellix.com/en-us/security-awareness/cybersecurity.html)

- [Udemy, inside SOC](https://www.udemy.com/course/cybersecurity-inside-a-security-operations-center/?couponCode=7A1C5415FE4B6DAF0DC7)

- [Splunk free courses](https://www.splunk.com/en_us/training/course-catalog.html?sort=Newest&filters=filterGroup1FreeCourses)

- [Tuto Splunk](https://geek-university.com/splunk-online-tutorial/)
