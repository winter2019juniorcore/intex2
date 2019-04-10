from django.db import models

# Create your models here.
class prescriber(models.Model):
    DoctorID = models.IntegerField(max_length=40)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    gender = models.CharField()
    state = models.CharField()
    credentials = models.CharField()
    specialty = models.CharField()
    OpioidPrescriber = models.IntegerField(max_length=1)
    totalprescriptions = models.IntegerField(max_length=2000)
    abilify = models.IntegerField(max_length=1000)
    ACETAMINOPHEN.CODEINE = models.IntegerField(max_length=1000)
    ACYCLOVIR = models.IntegerField(max_length=1000)
    ADVAIR.DISKUS = models.IntegerField(max_length=1000)
    AGGRENOX = models.IntegerField(max_length=1000)
    ALENDRONATE.SODIUM = models.IntegerField(max_length=1000)
    ALLOPURINOL = models.IntegerField(max_length=1000)
    ALPRAZOLAM = models.IntegerField(max_length=1000)
    AMIODARONE.HCL = models.IntegerField(max_length=1000)
    AMITRIPTYLINE.HCL = models.IntegerField(max_length=1000)
    AMLODIPINE.BESYLATE = models.IntegerField(max_length=1000)
    AMLODIPINE.BESYLATE.BENAZEPRIL = models.IntegerField(max_length=1000)
    AMOXICILLIN = models.IntegerField(max_length=1000)
    AMOX.TR.POTASSIUM.CLAVULANATE = models.IntegerField(max_length=1000)
    AMPHETAMINE.SALT.COMBO = models.IntegerField(max_length=1000)
    ATENOLOL = models.IntegerField(max_length=1000)
    ATORVASTATIN.CALCIUM = models.IntegerField(max_length=1000)
    AVODART = models.IntegerField(max_length=1000)
    AZITHROMYCIN = models.IntegerField(max_length=1000)
    BACLOFEN = models.IntegerField(max_length=1000)
    BD.ULTRA.FINE.PEN.NEEDLE = models.IntegerField(max_length=1000)
    BENAZEPRIL.HCL = models.IntegerField(max_length=1000)
    BENICAR = models.IntegerField(max_length=1000)
    BENICAR.HCT = models.IntegerField(max_length=1000)
    BENZTROPINE.MESYLATE = models.IntegerField(max_length=1000)
    BISOPROLOL.HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    BRIMONIDINE.TARTRATE = models.IntegerField(max_length=1000)
    BUMETANIDE = models.IntegerField(max_length=1000)
    BUPROPION.HCL.SR = models.IntegerField(max_length=1000)
    BUPROPION.XL = models.IntegerField(max_length=1000)
    BUSPIRONE.HCL = models.IntegerField(max_length=1000)
    BYSTOLIC = models.IntegerField(max_length=1000)
    CARBAMAZEPINE = models.IntegerField(max_length=1000)
    CARBIDOPA.LEVODOPA = models.IntegerField(max_length=1000)
    CARISOPRODOL = models.IntegerField(max_length=1000)
    CARTIA.XT = models.IntegerField(max_length=1000)
    CARVEDILOL = models.IntegerField(max_length=1000)
    CEFUROXIME = models.IntegerField(max_length=1000)
    CELEBREX = models.IntegerField(max_length=1000)
    CEPHALEXIN = models.IntegerField(max_length=1000)
    CHLORHEXIDINE.GLUCONATE = models.IntegerField(max_length=1000)
    CHLORTHALIDONE = models.IntegerField(max_length=1000)
    CILOSTAZOL = models.IntegerField(max_length=1000)
    CIPROFLOXACIN.HCL = models.IntegerField(max_length=1000)
    CITALOPRAM.HBR = models.IntegerField(max_length=1000)
    CLINDAMYCIN.HCL = models.IntegerField(max_length=1000)
    CLOBETASOL.PROPIONATE = models.IntegerField(max_length=1000)
    CLONAZEPAM = models.IntegerField(max_length=1000)
    CLONIDINE.HCL = models.IntegerField(max_length=1000)
    CLOPIDOGREL = models.IntegerField(max_length=1000)
    CLOTRIMAZOLE.BETAMETHASONE = models.IntegerField(max_length=1000)
    COLCRYS = models.IntegerField(max_length=1000)
    COMBIVENT.RESPIMAT = models.IntegerField(max_length=1000)
    CRESTOR = models.IntegerField(max_length=1000)
    CYCLOBENZAPRINE.HCL = models.IntegerField(max_length=1000)
    DEXILANT = models.IntegerField(max_length=1000)
    DIAZEPAM = models.IntegerField(max_length=1000)
    DICLOFENAC.SODIUM = models.IntegerField(max_length=1000)
    DICYCLOMINE.HCL = models.IntegerField(max_length=1000)
    DIGOX = models.IntegerField(max_length=1000)
    DIGOXIN = models.IntegerField(max_length=1000)
    DILTIAZEM.24HR.CD = models.IntegerField(max_length=1000)
    DILTIAZEM.24HR.ER = models.IntegerField(max_length=1000)
    DILTIAZEM.ER = models.IntegerField(max_length=1000)
    DILTIAZEM.HCL = models.IntegerField(max_length=1000)
    DIOVAN = models.IntegerField(max_length=1000)
    DIPHENOXYLATE.ATROPINE = models.IntegerField(max_length=1000)
    DIVALPROEX.SODIUM = models.IntegerField(max_length=1000)
    DIVALPROEX.SODIUM.ER = models.IntegerField(max_length=1000)
    DONEPEZIL.HCL = models.IntegerField(max_length=1000)
    DORZOLAMIDE.TIMOLOL = models.IntegerField(max_length=1000)
    DOXAZOSIN.MESYLATE = models.IntegerField(max_length=1000)
    DOXEPIN.HCL = models.IntegerField(max_length=1000)
    DOXYCYCLINE.HYCLATE = models.IntegerField(max_length=1000)
    DULOXETINE.HCL = models.IntegerField(max_length=1000)
    ENALAPRIL.MALEATE = models.IntegerField(max_length=1000)
    ESCITALOPRAM.OXALATE = models.IntegerField(max_length=1000)
    ESTRADIOL = models.IntegerField(max_length=1000)
    EXELON = models.IntegerField(max_length=1000)
    FAMOTIDINE = models.IntegerField(max_length=1000)
    FELODIPINE.ER = models.IntegerField(max_length=1000)
    FENOFIBRATE = models.IntegerField(max_length=1000)
    FENTANYL = models.IntegerField(max_length=1000)
    FINASTERIDE = models.IntegerField(max_length=1000)
    FLOVENT.HFA = models.IntegerField(max_length=1000)
    FLUCONAZOLE = models.IntegerField(max_length=1000)
    FLUOXETINE.HCL = models.IntegerField(max_length=1000)
    FLUTICASONE.PROPIONATE = models.IntegerField(max_length=1000)
    FUROSEMIDE = models.IntegerField(max_length=1000)
    GABAPENTIN = models.IntegerField(max_length=1000)
    GEMFIBROZIL = models.IntegerField(max_length=1000)
    GLIMEPIRIDE = models.IntegerField(max_length=1000)
    GLIPIZIDE = models.IntegerField(max_length=1000)
    GLIPIZIDE.ER = models.IntegerField(max_length=1000)
    GLIPIZIDE.XL = models.IntegerField(max_length=1000)
    GLYBURIDE = models.IntegerField(max_length=1000)
    HALOPERIDOL = models.IntegerField(max_length=1000)
    HUMALOG = models.IntegerField(max_length=1000)
    HYDRALAZINE.HCL = models.IntegerField(max_length=1000)
    HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    HYDROCODONE.ACETAMINOPHEN = models.IntegerField(max_length=1000)
    HYDROCORTISONE = models.IntegerField(max_length=1000)
    HYDROMORPHONE.HCL = models.IntegerField(max_length=1000)
    HYDROXYZINE.HCL = models.IntegerField(max_length=1000)
    IBANDRONATE.SODIUM = models.IntegerField(max_length=1000)
    IBUPROFEN = models.IntegerField(max_length=1000)
    INSULIN.SYRINGE = models.IntegerField(max_length=1000)
    IPRATROPIUM.BROMIDE = models.IntegerField(max_length=1000)
    IRBESARTAN = models.IntegerField(max_length=1000)
    ISOSORBIDE.MONONITRATE.ER = models.IntegerField(max_length=1000)
    JANTOVEN = models.IntegerField(max_length=1000)
    JANUMET = models.IntegerField(max_length=1000)
    JANUVIA = models.IntegerField(max_length=1000)
    KETOCONAZOLE = models.IntegerField(max_length=1000)
    KLOR.CON.10 = models.IntegerField(max_length=1000)
    KLOR.CON.M10 = models.IntegerField(max_length=1000)
    KLOR.CON.M20 = models.IntegerField(max_length=1000)
    LABETALOL.HCL = models.IntegerField(max_length=1000)
    LACTULOSE = models.IntegerField(max_length=1000)
    LAMOTRIGINE = models.IntegerField(max_length=1000)
    LANSOPRAZOLE = models.IntegerField(max_length=1000)
    LANTUS = models.IntegerField(max_length=1000)
    LANTUS.SOLOSTAR = models.IntegerField(max_length=1000)
    LATANOPROST = models.IntegerField(max_length=1000)
    LEVEMIR = models.IntegerField(max_length=1000)
    LEVEMIR.FLEXPEN = models.IntegerField(max_length=1000)
    LEVETIRACETAM = models.IntegerField(max_length=1000)
    LEVOFLOXACIN = models.IntegerField(max_length=1000)
    LEVOTHYROXINE.SODIUM = models.IntegerField(max_length=1000)
    LIDOCAINE = models.IntegerField(max_length=1000)
    LISINOPRIL = models.IntegerField(max_length=1000)
    LISINOPRIL.HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    LITHIUM.CARBONATE = models.IntegerField(max_length=1000)
    LORAZEPAM = models.IntegerField(max_length=1000)
    LOSARTAN.HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    LOSARTAN.POTASSIUM = models.IntegerField(max_length=1000)
    LOVASTATIN = models.IntegerField(max_length=1000)
    LOVAZA = models.IntegerField(max_length=1000)
    LUMIGAN = models.IntegerField(max_length=1000)
    LYRICA = models.IntegerField(max_length=1000)
    MECLIZINE.HCL = models.IntegerField(max_length=1000)
    MELOXICAM = models.IntegerField(max_length=1000)
    METFORMIN.HCL = models.IntegerField(max_length=1000)
    METFORMIN.HCL.ER = models.IntegerField(max_length=1000)
    METHADONE.HCL = models.IntegerField(max_length=1000)
    METHOCARBAMOL = models.IntegerField(max_length=1000)
    METHOTREXATE = models.IntegerField(max_length=1000)
    METHYLPREDNISOLONE = models.IntegerField(max_length=1000)
    METOCLOPRAMIDE.HCL = models.IntegerField(max_length=1000)
    METOLAZONE = models.IntegerField(max_length=1000)
    METOPROLOL.SUCCINATE = models.IntegerField(max_length=1000)
    METOPROLOL.TARTRATE = models.IntegerField(max_length=1000)
    METRONIDAZOLE = models.IntegerField(max_length=1000)
    MIRTAZAPINE = models.IntegerField(max_length=1000)
    MONTELUKAST.SODIUM = models.IntegerField(max_length=1000)
    MORPHINE.SULFATE = models.IntegerField(max_length=1000)
    MORPHINE.SULFATE.ER = models.IntegerField(max_length=1000)
    MUPIROCIN = models.IntegerField(max_length=1000)
    NABUMETONE = models.IntegerField(max_length=1000)
    NAMENDA = models.IntegerField(max_length=1000)
    NAMENDA.XR = models.IntegerField(max_length=1000)
    NAPROXEN = models.IntegerField(max_length=1000)
    NASONEX = models.IntegerField(max_length=1000)
    NEXIUM = models.IntegerField(max_length=1000)
    NIACIN.ER = models.IntegerField(max_length=1000)
    NIFEDICAL.XL = models.IntegerField(max_length=1000)
    NIFEDIPINE.ER = models.IntegerField(max_length=1000)
    NITROFURANTOIN.MONO.MACRO = models.IntegerField(max_length=1000)
    NITROSTAT = models.IntegerField(max_length=1000)
    NORTRIPTYLINE.HCL = models.IntegerField(max_length=1000)
    NOVOLOG = models.IntegerField(max_length=1000)
    NOVOLOG.FLEXPEN = models.IntegerField(max_length=1000)
    NYSTATIN = models.IntegerField(max_length=1000)
    OLANZAPINE = models.IntegerField(max_length=1000)
    OMEPRAZOLE = models.IntegerField(max_length=1000)
    ONDANSETRON.HCL = models.IntegerField(max_length=1000)
    ONDANSETRON.ODT = models.IntegerField(max_length=1000)
    ONGLYZA = models.IntegerField(max_length=1000)
    OXCARBAZEPINE = models.IntegerField(max_length=1000)
    OXYBUTYNIN.CHLORIDE = models.IntegerField(max_length=1000)
    OXYBUTYNIN.CHLORIDE.ER = models.IntegerField(max_length=1000)
    OXYCODONE.ACETAMINOPHEN = models.IntegerField(max_length=1000)
    OXYCODONE.HCL = models.IntegerField(max_length=1000)
    OXYCONTIN = models.IntegerField(max_length=1000)
    PANTOPRAZOLE.SODIUM = models.IntegerField(max_length=1000)
    PAROXETINE.HCL = models.IntegerField(max_length=1000)
    PHENOBARBITAL = models.IntegerField(max_length=1000)
    PHENYTOIN.SODIUM.EXTENDED = models.IntegerField(max_length=1000)
    PIOGLITAZONE.HCL = models.IntegerField(max_length=1000)
    POLYETHYLENE.GLYCOL.3350 = models.IntegerField(max_length=1000)
    POTASSIUM.CHLORIDE = models.IntegerField(max_length=1000)
    PRADAXA = models.IntegerField(max_length=1000)
    PRAMIPEXOLE.DIHYDROCHLORIDE = models.IntegerField(max_length=1000)
    PRAVASTATIN.SODIUM = models.IntegerField(max_length=1000)
    PREDNISONE = models.IntegerField(max_length=1000)
    PREMARIN = models.IntegerField(max_length=1000)
    PRIMIDONE = models.IntegerField(max_length=1000)
    PROAIR.HFA = models.IntegerField(max_length=1000)
    PROMETHAZINE.HCL = models.IntegerField(max_length=1000)
    PROPRANOLOL.HCL = models.IntegerField(max_length=1000)
    PROPRANOLOL.HCL.ER = models.IntegerField(max_length=1000)
    QUETIAPINE.FUMARATE = models.IntegerField(max_length=1000)
    QUINAPRIL.HCL = models.IntegerField(max_length=1000)
    RALOXIFENE.HCL = models.IntegerField(max_length=1000)
    RAMIPRIL = models.IntegerField(max_length=1000)
    RANEXA = models.IntegerField(max_length=1000)
    RANITIDINE.HCL = models.IntegerField(max_length=1000)
    RESTASIS = models.IntegerField(max_length=1000)
    RISPERIDONE = models.IntegerField(max_length=1000)
    ROPINIROLE.HCL = models.IntegerField(max_length=1000)
    SEROQUEL.XR = models.IntegerField(max_length=1000)
    SERTRALINE.HCL = models.IntegerField(max_length=1000)
    SIMVASTATIN = models.IntegerField(max_length=1000)
    SOTALOL = models.IntegerField(max_length=1000)
    SPIRIVA = models.IntegerField(max_length=1000)
    SPIRONOLACTONE = models.IntegerField(max_length=1000)
    SUCRALFATE = models.IntegerField(max_length=1000)
    SULFAMETHOXAZOLE.TRIMETHOPRIM = models.IntegerField(max_length=1000)
    SUMATRIPTAN.SUCCINATE = models.IntegerField(max_length=1000)
    SYMBICORT = models.IntegerField(max_length=1000)
    SYNTHROID = models.IntegerField(max_length=1000)
    TAMSULOSIN.HCL = models.IntegerField(max_length=1000)
    TEMAZEPAM = models.IntegerField(max_length=1000)
    TERAZOSIN.HCL = models.IntegerField(max_length=1000)
    TIMOLOL.MALEATE = models.IntegerField(max_length=1000)
    TIZANIDINE.HCL = models.IntegerField(max_length=1000)
    TOLTERODINE.TARTRATE.ER = models.IntegerField(max_length=1000)
    TOPIRAMATE = models.IntegerField(max_length=1000)
    TOPROL.XL = models.IntegerField(max_length=1000)
    TORSEMIDE = models.IntegerField(max_length=1000)
    TRAMADOL.HCL = models.IntegerField(max_length=1000)
    TRAVATAN.Z = models.IntegerField(max_length=1000)
    TRAZODONE.HCL = models.IntegerField(max_length=1000)
    TRIAMCINOLONE.ACETONIDE = models.IntegerField(max_length=1000)
    TRIAMTERENE.HYDROCHLOROTHIAZID = models.IntegerField(max_length=1000)
    VALACYCLOVIR = models.IntegerField(max_length=1000)
    VALSARTAN = models.IntegerField(max_length=1000)
    VALSARTAN.HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    VENLAFAXINE.HCL = models.IntegerField(max_length=1000)
    VENLAFAXINE.HCL.ER = models.IntegerField(max_length=1000)
    VENTOLIN.HFA = models.IntegerField(max_length=1000)
    VERAPAMIL.ER = models.IntegerField(max_length=1000)
    VESICARE = models.IntegerField(max_length=1000)
    VOLTAREN = models.IntegerField(max_length=1000)
    VYTORIN = models.IntegerField(max_length=1000)
    WARFARIN.SODIUM = models.IntegerField(max_length=1000)
    XARELTO = models.IntegerField(max_length=1000)
    ZETIA = models.IntegerField(max_length=1000)
    ZIPRASIDONE.HCL = models.IntegerField(max_length=1000)
    ZOLPIDEM.TARTRATE = models.IntegerField(max_length=1000)

    def __str__(self):
        return ' %s %s %s %s %s %s %s %s %s ' % (self.DoctorID, self.fname, self.lname, self.gender, self.state, self.credentials, self.specialty, self.OpioidPrescriber, self.totalprescriptions)
    
class overdoses(models.Model):
        state = models.CharField(max_length=200)
        population = models.CharField()
        deaths = models.CharField()
        abbrev = models.CharField()
    def __str__(self):
        return ' %s %s %s %s ' % (self.state, self.population, self.deaths, self.abbrev)

class docdrugqty(models.Model):
    DoctorID = models.IntegerField()
    drug = models.CharField()
    qty = models.IntegerField()
    def __str__(self):
        return ' %s %s %s ' % (self.DoctorID, self.drug, self.qty)

class dangerscore (models.Model):
    DoctorID = models.IntegerField()
    dangerscore = models.IntegerField()

    def __str__(self):
        return ' %s %s %s ' % (self.DoctorID, self.dangerscore)