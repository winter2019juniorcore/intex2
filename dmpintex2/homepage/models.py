from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class prescriber(models.Model):
    DoctorID = models.IntegerField(max_length=40)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    credentials = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    OpioidPrescriber = models.IntegerField(max_length=1)
    totalprescriptions = models.IntegerField(max_length=2000)
    abilify = models.IntegerField(max_length=1000)
    ACETAMINOPHENCODEINE = models.IntegerField(max_length=1000)
    ACYCLOVIR = models.IntegerField(max_length=1000)
    ADVAIRDISKUS = models.IntegerField(max_length=1000)
    AGGRENOX = models.IntegerField(max_length=1000)
    ALENDRONATESODIUM = models.IntegerField(max_length=1000)
    ALLOPURINOL = models.IntegerField(max_length=1000)
    ALPRAZOLAM = models.IntegerField(max_length=1000)
    AMIODARONEHCL = models.IntegerField(max_length=1000)
    AMITRIPTYLINEHCL = models.IntegerField(max_length=1000)
    AMLODIPINEBESYLATE = models.IntegerField(max_length=1000)
    AMLODIPINEBESYLATEBENAZEPRIL = models.IntegerField(max_length=1000)
    AMOXICILLIN = models.IntegerField(max_length=1000)
    AMOXTRPOTASSIUMCLAVULANATE = models.IntegerField(max_length=1000)
    AMPHETAMINESALTCOMBO = models.IntegerField(max_length=1000)
    ATENOLOL = models.IntegerField(max_length=1000)
    ATORVASTATINCALCIUM = models.IntegerField(max_length=1000)
    AVODART = models.IntegerField(max_length=1000)
    AZITHROMYCIN = models.IntegerField(max_length=1000)
    BACLOFEN = models.IntegerField(max_length=1000)
    BDULTRAFINEPENNEEDLE = models.IntegerField(max_length=1000)
    BENAZEPRILHCL = models.IntegerField(max_length=1000)
    BENICAR = models.IntegerField(max_length=1000)
    BENICARHCT = models.IntegerField(max_length=1000)
    BENZTROPINEMESYLATE = models.IntegerField(max_length=1000)
    BISOPROLOLHYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    BRIMONIDINETARTRATE = models.IntegerField(max_length=1000)
    BUMETANIDE = models.IntegerField(max_length=1000)
    BUPROPIONHCLSR = models.IntegerField(max_length=1000)
    BUPROPIONXL = models.IntegerField(max_length=1000)
    BUSPIRONEHCL = models.IntegerField(max_length=1000)
    BYSTOLIC = models.IntegerField(max_length=1000)
    CARBAMAZEPINE = models.IntegerField(max_length=1000)
    CARBIDOPALEVODOPA = models.IntegerField(max_length=1000)
    CARISOPRODOL = models.IntegerField(max_length=1000)
    CARTIAXT = models.IntegerField(max_length=1000)
    CARVEDILOL = models.IntegerField(max_length=1000)
    CEFUROXIME = models.IntegerField(max_length=1000)
    CELEBREX = models.IntegerField(max_length=1000)
    CEPHALEXIN = models.IntegerField(max_length=1000)
    CHLORHEXIDINEGLUCONATE = models.IntegerField(max_length=1000)
    CHLORTHALIDONE = models.IntegerField(max_length=1000)
    CILOSTAZOL = models.IntegerField(max_length=1000)
    CIPROFLOXACINHCL = models.IntegerField(max_length=1000)
    CITALOPRAMHBR = models.IntegerField(max_length=1000)
    CLINDAMYCINHCL = models.IntegerField(max_length=1000)
    CLOBETASOLPROPIONATE = models.IntegerField(max_length=1000)
    CLONAZEPAM = models.IntegerField(max_length=1000)
    CLONIDINEHCL = models.IntegerField(max_length=1000)
    CLOPIDOGREL = models.IntegerField(max_length=1000)
    CLOTRIMAZOLEBETAMETHASONE = models.IntegerField(max_length=1000)
    COLCRYS = models.IntegerField(max_length=1000)
    COMBIVENTRESPIMAT = models.IntegerField(max_length=1000)
    CRESTOR = models.IntegerField(max_length=1000)
    CYCLOBENZAPRINEHCL = models.IntegerField(max_length=1000)
    DEXILANT = models.IntegerField(max_length=1000)
    DIAZEPAM = models.IntegerField(max_length=1000)
    DICLOFENACSODIUM = models.IntegerField(max_length=1000)
    DICYCLOMINEHCL = models.IntegerField(max_length=1000)
    DIGOX = models.IntegerField(max_length=1000)
    DIGOXIN = models.IntegerField(max_length=1000)
    DILTIAZEM24HRCD = models.IntegerField(max_length=1000)
    DILTIAZEM24HRER = models.IntegerField(max_length=1000)
    DILTIAZEMER = models.IntegerField(max_length=1000)
    DILTIAZEMHCL = models.IntegerField(max_length=1000)
    DIOVAN = models.IntegerField(max_length=1000)
    DIPHENOXYLATEATROPINE = models.IntegerField(max_length=1000)
    DIVALPROEXSODIUM = models.IntegerField(max_length=1000)
    DIVALPROEXSODIUMER = models.IntegerField(max_length=1000)
    DONEPEZILHCL = models.IntegerField(max_length=1000)
    DORZOLAMIDETIMOLOL = models.IntegerField(max_length=1000)
    DOXAZOSINMESYLATE = models.IntegerField(max_length=1000)
    DOXEPINHCL = models.IntegerField(max_length=1000)
    DOXYCYCLINEHYCLATE = models.IntegerField(max_length=1000)
    DULOXETINEHCL = models.IntegerField(max_length=1000)
    ENALAPRILMALEATE = models.IntegerField(max_length=1000)
    ESCITALOPRAMOXALATE = models.IntegerField(max_length=1000)
    ESTRADIOL = models.IntegerField(max_length=1000)
    EXELON = models.IntegerField(max_length=1000)
    FAMOTIDINE = models.IntegerField(max_length=1000)
    FELODIPINEER = models.IntegerField(max_length=1000)
    FENOFIBRATE = models.IntegerField(max_length=1000)
    FENTANYL = models.IntegerField(max_length=1000)
    FINASTERIDE = models.IntegerField(max_length=1000)
    FLOVENTHFA = models.IntegerField(max_length=1000)
    FLUCONAZOLE = models.IntegerField(max_length=1000)
    FLUOXETINEHCL = models.IntegerField(max_length=1000)
    FLUTICASONEPROPIONATE = models.IntegerField(max_length=1000)
    FUROSEMIDE = models.IntegerField(max_length=1000)
    GABAPENTIN = models.IntegerField(max_length=1000)
    GEMFIBROZIL = models.IntegerField(max_length=1000)
    GLIMEPIRIDE = models.IntegerField(max_length=1000)
    GLIPIZIDE = models.IntegerField(max_length=1000)
    GLIPIZIDEER = models.IntegerField(max_length=1000)
    GLIPIZIDEXL = models.IntegerField(max_length=1000)
    GLYBURIDE = models.IntegerField(max_length=1000)
    HALOPERIDOL = models.IntegerField(max_length=1000)
    HUMALOG = models.IntegerField(max_length=1000)
    HYDRALAZINEHCL = models.IntegerField(max_length=1000)
    HYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    HYDROCODONEACETAMINOPHEN = models.IntegerField(max_length=1000)
    HYDROCORTISONE = models.IntegerField(max_length=1000)
    HYDROMORPHONEHCL = models.IntegerField(max_length=1000)
    HYDROXYZINEHCL = models.IntegerField(max_length=1000)
    IBANDRONATESODIUM = models.IntegerField(max_length=1000)
    IBUPROFEN = models.IntegerField(max_length=1000)
    INSULINSYRINGE = models.IntegerField(max_length=1000)
    IPRATROPIUMBROMIDE = models.IntegerField(max_length=1000)
    IRBESARTAN = models.IntegerField(max_length=1000)
    ISOSORBIDEMONONITRATEER = models.IntegerField(max_length=1000)
    JANTOVEN = models.IntegerField(max_length=1000)
    JANUMET = models.IntegerField(max_length=1000)
    JANUVIA = models.IntegerField(max_length=1000)
    KETOCONAZOLE = models.IntegerField(max_length=1000)
    KLORCON10 = models.IntegerField(max_length=1000)
    KLORCONM10 = models.IntegerField(max_length=1000)
    KLORCONM20 = models.IntegerField(max_length=1000)
    LABETALOLHCL = models.IntegerField(max_length=1000)
    LACTULOSE = models.IntegerField(max_length=1000)
    LAMOTRIGINE = models.IntegerField(max_length=1000)
    LANSOPRAZOLE = models.IntegerField(max_length=1000)
    LANTUS = models.IntegerField(max_length=1000)
    LANTUSSOLOSTAR = models.IntegerField(max_length=1000)
    LATANOPROST = models.IntegerField(max_length=1000)
    LEVEMIR = models.IntegerField(max_length=1000)
    LEVEMIRFLEXPEN = models.IntegerField(max_length=1000)
    LEVETIRACETAM = models.IntegerField(max_length=1000)
    LEVOFLOXACIN = models.IntegerField(max_length=1000)
    LEVOTHYROXINESODIUM = models.IntegerField(max_length=1000)
    LIDOCAINE = models.IntegerField(max_length=1000)
    LISINOPRIL = models.IntegerField(max_length=1000)
    LISINOPRILHYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    LITHIUMCARBONATE = models.IntegerField(max_length=1000)
    LORAZEPAM = models.IntegerField(max_length=1000)
    LOSARTANHYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    LOSARTANPOTASSIUM = models.IntegerField(max_length=1000)
    LOVASTATIN = models.IntegerField(max_length=1000)
    LOVAZA = models.IntegerField(max_length=1000)
    LUMIGAN = models.IntegerField(max_length=1000)
    LYRICA = models.IntegerField(max_length=1000)
    MECLIZINEHCL = models.IntegerField(max_length=1000)
    MELOXICAM = models.IntegerField(max_length=1000)
    METFORMINHCL = models.IntegerField(max_length=1000)
    METFORMINHCLER = models.IntegerField(max_length=1000)
    METHADONEHCL = models.IntegerField(max_length=1000)
    METHOCARBAMOL = models.IntegerField(max_length=1000)
    METHOTREXATE = models.IntegerField(max_length=1000)
    METHYLPREDNISOLONE = models.IntegerField(max_length=1000)
    METOCLOPRAMIDEHCL = models.IntegerField(max_length=1000)
    METOLAZONE = models.IntegerField(max_length=1000)
    METOPROLOLSUCCINATE = models.IntegerField(max_length=1000)
    METOPROLOLTARTRATE = models.IntegerField(max_length=1000)
    METRONIDAZOLE = models.IntegerField(max_length=1000)
    MIRTAZAPINE = models.IntegerField(max_length=1000)
    MONTELUKASTSODIUM = models.IntegerField(max_length=1000)
    MORPHINESULFATE = models.IntegerField(max_length=1000)
    MORPHINESULFATE.ER = models.IntegerField(max_length=1000)
    MUPIROCIN = models.IntegerField(max_length=1000)
    NABUMETONE = models.IntegerField(max_length=1000)
    NAMENDA = models.IntegerField(max_length=1000)
    NAMENDAXR = models.IntegerField(max_length=1000)
    NAPROXEN = models.IntegerField(max_length=1000)
    NASONEX = models.IntegerField(max_length=1000)
    NEXIUM = models.IntegerField(max_length=1000)
    NIACINER = models.IntegerField(max_length=1000)
    NIFEDICALXL = models.IntegerField(max_length=1000)
    NIFEDIPINEER = models.IntegerField(max_length=1000)
    NITROFURANTOINMONOMACRO = models.IntegerField(max_length=1000)
    NITROSTAT = models.IntegerField(max_length=1000)
    NORTRIPTYLINEHCL = models.IntegerField(max_length=1000)
    NOVOLOG = models.IntegerField(max_length=1000)
    NOVOLOGFLEXPEN = models.IntegerField(max_length=1000)
    NYSTATIN = models.IntegerField(max_length=1000)
    OLANZAPINE = models.IntegerField(max_length=1000)
    OMEPRAZOLE = models.IntegerField(max_length=1000)
    ONDANSETRONHCL = models.IntegerField(max_length=1000)
    ONDANSETRONODT = models.IntegerField(max_length=1000)
    ONGLYZA = models.IntegerField(max_length=1000)
    OXCARBAZEPINE = models.IntegerField(max_length=1000)
    OXYBUTYNINCHLORIDE = models.IntegerField(max_length=1000)
    OXYBUTYNINCHLORIDEER = models.IntegerField(max_length=1000)
    OXYCODONEACETAMINOPHEN = models.IntegerField(max_length=1000)
    OXYCODONEHCL = models.IntegerField(max_length=1000)
    OXYCONTIN = models.IntegerField(max_length=1000)
    PANTOPRAZOLESODIUM = models.IntegerField(max_length=1000)
    PAROXETINEHCL = models.IntegerField(max_length=1000)
    PHENOBARBITAL = models.IntegerField(max_length=1000)
    PHENYTOINSODIUMEXTENDED = models.IntegerField(max_length=1000)
    PIOGLITAZONEHCL = models.IntegerField(max_length=1000)
    POLYETHYLENEGLYCOL3350 = models.IntegerField(max_length=1000)
    POTASSIUMCHLORIDE = models.IntegerField(max_length=1000)
    PRADAXA = models.IntegerField(max_length=1000)
    PRAMIPEXOLEDIHYDROCHLORIDE = models.IntegerField(max_length=1000)
    PRAVASTATINSODIUM = models.IntegerField(max_length=1000)
    PREDNISONE = models.IntegerField(max_length=1000)
    PREMARIN = models.IntegerField(max_length=1000)
    PRIMIDONE = models.IntegerField(max_length=1000)
    PROAIRHFA = models.IntegerField(max_length=1000)
    PROMETHAZINEHCL = models.IntegerField(max_length=1000)
    PROPRANOLOLHCL = models.IntegerField(max_length=1000)
    PROPRANOLOLHCLER = models.IntegerField(max_length=1000)
    QUETIAPINEFUMARATE = models.IntegerField(max_length=1000)
    QUINAPRILHCL = models.IntegerField(max_length=1000)
    RALOXIFENEHCL = models.IntegerField(max_length=1000)
    RAMIPRIL = models.IntegerField(max_length=1000)
    RANEXA = models.IntegerField(max_length=1000)
    RANITIDINEHCL = models.IntegerField(max_length=1000)
    RESTASIS = models.IntegerField(max_length=1000)
    RISPERIDONE = models.IntegerField(max_length=1000)
    ROPINIROLEHCL = models.IntegerField(max_length=1000)
    SEROQUELXR = models.IntegerField(max_length=1000)
    SERTRALINEHCL = models.IntegerField(max_length=1000)
    SIMVASTATIN = models.IntegerField(max_length=1000)
    SOTALOL = models.IntegerField(max_length=1000)
    SPIRIVA = models.IntegerField(max_length=1000)
    SPIRONOLACTONE = models.IntegerField(max_length=1000)
    SUCRALFATE = models.IntegerField(max_length=1000)
    SULFAMETHOXAZOLETRIMETHOPRIM = models.IntegerField(max_length=1000)
    SUMATRIPTANSUCCINATE = models.IntegerField(max_length=1000)
    SYMBICORT = models.IntegerField(max_length=1000)
    SYNTHROID = models.IntegerField(max_length=1000)
    TAMSULOSINHCL = models.IntegerField(max_length=1000)
    TEMAZEPAM = models.IntegerField(max_length=1000)
    TERAZOSINHCL = models.IntegerField(max_length=1000)
    TIMOLOLMALEATE = models.IntegerField(max_length=1000)
    TIZANIDINEHCL = models.IntegerField(max_length=1000)
    TOLTERODINETARTRATEER = models.IntegerField(max_length=1000)
    TOPIRAMATE = models.IntegerField(max_length=1000)
    TOPROLXL = models.IntegerField(max_length=1000)
    TORSEMIDE = models.IntegerField(max_length=1000)
    TRAMADOLHCL = models.IntegerField(max_length=1000)
    TRAVATANZ = models.IntegerField(max_length=1000)
    TRAZODONEHCL = models.IntegerField(max_length=1000)
    TRIAMCINOLONEACETONIDE = models.IntegerField(max_length=1000)
    TRIAMTERENEHYDROCHLOROTHIAZID = models.IntegerField(max_length=1000)
    VALACYCLOVIR = models.IntegerField(max_length=1000)
    VALSARTAN = models.IntegerField(max_length=1000)
    VALSARTANHYDROCHLOROTHIAZIDE = models.IntegerField(max_length=1000)
    VENLAFAXINEHCL = models.IntegerField(max_length=1000)
    VENLAFAXINEHCLER = models.IntegerField(max_length=1000)
    VENTOLINHFA = models.IntegerField(max_length=1000)
    VERAPAMILER = models.IntegerField(max_length=1000)
    VESICARE = models.IntegerField(max_length=1000)
    VOLTAREN = models.IntegerField(max_length=1000)
    VYTORIN = models.IntegerField(max_length=1000)
    WARFARINSODIUM = models.IntegerField(max_length=1000)
    XARELTO = models.IntegerField(max_length=1000)
    ZETIA = models.IntegerField(max_length=1000)
    ZIPRASIDONEHCL = models.IntegerField(max_length=1000)
    ZOLPIDEMTARTRATE = models.IntegerField(max_length=1000)

    def __str__(self):
        return ' %s %s %s %s %s %s %s %s %s ' % (self.DoctorID, self.fname, self.lname, self.gender, self.state, self.credentials, self.specialty, self.OpioidPrescriber, self.totalprescriptions)
    
class overdoses(models.Model):
    state = models.CharField(max_length=200)
    population = models.CharField(max_length=30000)
    deaths = models.CharField(max_length=30000)
    abbrev = models.CharField(max_length=30000)
    def __str__(self):
        return ' %s %s %s %s ' % (self.state, self.population, self.deaths, self.abbrev)

class docdrugqty(models.Model):
    DoctorID = models.IntegerField()
    drug = models.CharField(max_length=300)
    qty = models.IntegerField()
    def __str__(self):
        return ' %s %s %s ' % (self.DoctorID, self.drug, self.qty)

class dangerscore(models.Model):
    DoctorID = models.IntegerField()
    dangerscore = models.IntegerField()

    def __str__(self):
        return ' %s %s ' % (self.DoctorID, self.dangerscore)