---
type: paper
uid: "2026-06-08-path-2-reconstruct-ourselves-on-individual-brain-maybe-initially-use-colin27-to-test-pipeline-we"
title: "Direct approach to compute Jacobians for diffuse optical tomography using perturbation Monte Carlo-based photon \"replay\""
authors: ["Yao R", "Intes X", "Fang Q"]
year: 2018
venue: "Biomed Opt Express"
doi: "10.1364/BOE.9.004588"
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC6179418/"
status: to-read
rating: 
shared_by: "AnthonyK"
channel: "live-zork"
tags: ["ai", "live-zork", "llm-enriched", "paper", "url"]
source: "url"
added: 2026-06-12
---
## Summary
Perturbation Monte Carlo (pMC) has been previously proposed to rapidly recompute optical measurements when small perturbations of optical properties are considered, but it was largely restricted to changes associated with prior tissue segments or regions-of-interest. In this work, we expand pMC to compute spatially and temporally resolved sensitivity profiles, i.e. the Jacobians, for diffuse optical tomography (DOT) applications. By recording the pseudo random number generator (PRNG) seeds of each detected photon, we are able to "replay" all detected photons to directly create the 3D sensitivity profiles for both absorption and scattering coefficients. We validate the replay-based Jacobians against the traditional adjoint Monte Carlo (aMC) method, and demonstrate the feasibility of using this approach for efficient 3D image reconstructions using in vitro hyperspectral wide-field DOT measurements. The strengths and limitations of the replay approach regarding its computational efficiency and accuracy are discussed, in comparison with aMC, for point-detector systems as well as wide-field pattern-based and hyperspectral imaging systems. The replay approach has been implemented in both of our open-source MC simulators - MCX and MMC (http://mcx.space).

## Key points
- Novel photon "replay" technique using PRNG seeds to compute 3D Jacobians for both absorption and scattering coefficients in DOT
- Extends pMC approach beyond region-of-interest constraints to spatially and temporally resolved sensitivity profiles
- Validation against traditional adjoint Monte Carlo method with analysis of computational efficiency and accuracy tradeoffs
- Implemented in open-source Monte Carlo simulators MCX and MMC for practical DOT applications
- Demonstrated feasibility for efficient 3D image reconstructions with in vitro hyperspectral wide-field DOT measurements

## Notes
Path 2: Reconstruct ourselves on individual brain (maybe initially use Colin27 to test pipeline). We currently have only a Jacobian that goes from intensity. However, we can com...

## Links
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC6179418/
- Discord: https://discord.com/channels/1400359609323229267/1513140538780549190/1513477255530152028

## My notes
-
