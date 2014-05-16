import ROOT

c1 = ROOT.TCanvas()
c1.SetGridx()
c1.SetGridy()
c1.SetTickx()
c1.SetTicky()

def getEff(file,dir,den,num):
    f = ROOT.TFile(file)
    t = f.Get(dir)
    h1 = ROOT.TH1F("h1","h1",40,1.5,2.5)
    t.Draw("abs(eta) >> h1",den)
    h2 = ROOT.TH1F("h2","h2",40,1.5,2.5)
    t.Draw("abs(eta) >> h2",num)
    e = ROOT.TEfficiency(h2,h1)
    return e

b1 = ROOT.TH1F("b1","b1",40,1.5,2.5)
b1.GetYaxis().SetRangeUser(0.88,1)
b1.GetYaxis().SetTitleOffset(1.2)
b1.GetYaxis().SetNdivisions(520)
b1.GetYaxis().SetTitle("LCT reconstruction efficiency")
b1.GetXaxis().SetTitle("#eta of simulated muon track")
b1.SetTitle(" "*64 + "CMS Simulation Preliminary")
b1.SetStats(0)

treename = "GEMCSCAnalyzer/trk_eff_ME11"
den = "has_csc_sh>0"
num = "has_csc_sh>0 && has_lct>0"

e1 = getEff("NEW_Analyzer_NEW_CSC4_All_eff.root",treename,den,num)
#e2 = getEff("GSA_CSC3_PU0.root",treename,den,num)
e3 = getEff("FEB14_AAgain_SLHC_eff.root",treename,den,num)
e4 = getEff("NEW_Analyzer_NEW_CSC4_Quality_FT_eff.root",treename,den,num)
#e5 = getEff("NEW_Analyzer_NEW_CSC4_SLHC_eff.root",treename,den,num)
e5 = getEff("FEB14_AAgain_SLHC_eff.root",treename,den,num)
e7 = getEff("FEB14_AAgain_Quality_eff.root",treename,den,num)

e1.SetLineColor(ROOT.kRed)
e1.SetLineWidth(2)
e3.SetLineColor(ROOT.kYellow)
e3.SetLineWidth(4)
e4.SetLineColor(ROOT.kBlue)
e4.SetLineWidth(2)
e5.SetLineColor(ROOT.kBlack)
e5.SetLineWidth(2)
#e6.SetLineColor(ROOT.kViolet-2)
#e6.SetLineWidth(2)
e7.SetLineColor(ROOT.kViolet-2)
e7.SetLineWidth(2)

b1.Draw()
e1.Draw("same")
#e2.Draw("same")
#e3.Draw("same")
#e4.Draw("same")
e5.Draw("same")
#e6.Draw("same")
e7.Draw("same")

legend = ROOT.TLegend(0.23,0.16,0.52,0.44)
legend.SetFillColor(ROOT.kWhite)
legend.SetHeader("PU140, New Release ")
legend.AddEntry(e1,"CSC4 L1 emulator, New Analyzer","l")
#legend.AddEntry(e2,"CSC Algorithm (3 hits)","l")
#legend.AddEntry(e3,"CBX","l")
#legend.AddEntry(e4,"By Quality_FT","l")
legend.AddEntry(e5,"CSC4 CBX","l")
#legend.AddEntry(e6,"GEM-CSC Algorithm (step 3)","l")
legend.AddEntry(e7,"CSC4 Quality","l")
legend.Draw("same")

c1.SaveAs("LCT_reco_eff_PU0.pdf")
c1.SaveAs("LCT_reco_eff_PU0.png")
