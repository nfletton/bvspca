
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:tns="http://www.petango.com/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" targetNamespace="http://www.petango.com/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <s:schema elementFormDefault="qualified" targetNamespace="http://www.petango.com/">
      <s:element name="MedicalViewReportPdf">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authKey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ftpDestination" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="MedicalViewReportPdfResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="MedicalViewReportPdfResult" type="s:boolean" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptionDetails">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authKey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptionDetailsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="AdoptionDetailsResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptionList">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="authKey" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="adoptionDate" type="s:dateTime" />
            <s:element minOccurs="0" maxOccurs="1" name="siteID" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptionListResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="AdoptionListResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="ArrayOfXmlNode">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="XmlNode" nillable="true">
            <s:complexType mixed="true">
              <s:sequence>
                <s:any />
              </s:sequence>
            </s:complexType>
          </s:element>
        </s:sequence>
      </s:complexType>
      <s:element name="AdoptableSearch">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="speciesID" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="location" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="site" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="onHold" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="primaryBreed" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="secondaryBreed" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="specialNeeds" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noDogs" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noCats" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noKids" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="stageID" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptableSearchResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="AdoptableSearchResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptableSearchWithStage">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="speciesID" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="location" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="site" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="onHold" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="primaryBreed" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="secondaryBreed" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="specialNeeds" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noDogs" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noCats" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="noKids" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="stageID" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="featured" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptableSearchWithStageResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="AdoptableSearchWithStageResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptableDetails">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="animalID" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="AdoptableDetailsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="AdoptableDetailsResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearch">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="searchOption" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundSearchResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchForCompanyGroup">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="searchOption" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchForCompanyGroupResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundSearchForCompanyGroupResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchForCompanyGroupPageable">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="searchOption" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="skip" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="take" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchForCompanyGroupPageableResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundSearchForCompanyGroupPageableResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchWithSite">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="searchOption" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="siteID" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundSearchWithSiteResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundSearchWithSiteResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearch">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearchResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="lostSearchResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearchForCompanyGroup">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearchForCompanyGroupResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="lostSearchForCompanyGroupResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearchForCompanyGroupPageable">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="speciesID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="sex" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="ageGroup" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
            <s:element minOccurs="0" maxOccurs="1" name="orderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="skip" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="take" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostSearchForCompanyGroupPageableResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="lostSearchForCompanyGroupPageableResult" type="tns:ArrayOfXmlNode" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundDetails">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundDetailsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundDetailsResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundDetailsForCompanyGroup">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="foundDetailsForCompanyGroupResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="foundDetailsForCompanyGroupResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostDetails">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostDetailsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="lostDetailsResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostDetailsForCompanyGroup">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="1" maxOccurs="1" name="animalID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="authkey" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="lostDetailsForCompanyGroupResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="lostDetailsForCompanyGroupResult">
              <s:complexType mixed="true">
                <s:sequence>
                  <s:any />
                </s:sequence>
              </s:complexType>
            </s:element>
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="HappyTailList">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="pAuthKey" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="pSpeciesID" type="s:int" />
            <s:element minOccurs="1" maxOccurs="1" name="pSiteID" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="pOrderBy" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="pCount" type="s:int" />
            <s:element minOccurs="0" maxOccurs="1" name="pFeaturedPet" type="s:string" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="HappyTailListResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="HappyTailListResult" type="tns:ArrayOfAnyType" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="ArrayOfAnyType">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="anyType" nillable="true" />
        </s:sequence>
      </s:complexType>
      <s:element name="HappyTailDetails">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="pAuthkey" type="s:string" />
            <s:element minOccurs="1" maxOccurs="1" name="pAdoptionID" type="s:int" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:complexType name="HappyTailListItem">
        <s:sequence>
          <s:element minOccurs="1" maxOccurs="1" name="AdoptionID" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="AdoptionDate" type="s:dateTime" />
          <s:element minOccurs="1" maxOccurs="1" name="HappyTExpiryDate" type="s:dateTime" />
          <s:element minOccurs="1" maxOccurs="1" name="AnimalID" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="CompanyID" type="s:int" />
          <s:element minOccurs="1" maxOccurs="1" name="ShelterID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="Name" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="Species" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="SpeciesID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="Sex" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="SiteID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="PostZipCode" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="DateOfBirth" type="s:dateTime" />
          <s:element minOccurs="0" maxOccurs="1" name="SpayedNeutered" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="SpecialNeeds" type="s:boolean" />
          <s:element minOccurs="0" maxOccurs="1" name="Size" type="s:string" />
          <s:element minOccurs="0" maxOccurs="1" name="PrimaryBreed" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="PrimaryBreedID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="SecondaryBreed" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="SecondaryBreedID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="AgeGroup" type="s:string" />
          <s:element minOccurs="1" maxOccurs="1" name="AgeGroupID" type="s:int" />
          <s:element minOccurs="0" maxOccurs="1" name="Photo" type="s:string" />
        </s:sequence>
      </s:complexType>
      <s:complexType name="HappyTailDetailItem">
        <s:complexContent mixed="false">
          <s:extension base="tns:HappyTailListItem">
            <s:sequence>
              <s:element minOccurs="0" maxOccurs="1" name="HouseTrained" type="s:string" />
              <s:element minOccurs="0" maxOccurs="1" name="PrimaryColor" type="s:string" />
              <s:element minOccurs="1" maxOccurs="1" name="PrimaryColorID" type="s:int" />
              <s:element minOccurs="0" maxOccurs="1" name="SecondaryColor" type="s:string" />
              <s:element minOccurs="1" maxOccurs="1" name="SecondaryColorID" type="s:int" />
              <s:element minOccurs="0" maxOccurs="1" name="Declawed" type="s:string" />
              <s:element minOccurs="0" maxOccurs="1" name="Photo2" type="s:string" />
              <s:element minOccurs="0" maxOccurs="1" name="Photo3" type="s:string" />
              <s:element minOccurs="0" maxOccurs="1" name="Memo" type="s:string" />
              <s:element minOccurs="0" maxOccurs="1" name="ShelterMicrosite" type="s:string" />
            </s:sequence>
          </s:extension>
        </s:complexContent>
      </s:complexType>
      <s:complexType name="ArrayOfHappyTailDetailItem">
        <s:sequence>
          <s:element minOccurs="0" maxOccurs="unbounded" name="HappyTailDetailItem" nillable="true" type="tns:HappyTailDetailItem" />
        </s:sequence>
      </s:complexType>
      <s:element name="HappyTailDetailsResponse">
        <s:complexType>
          <s:sequence>
            <s:element minOccurs="0" maxOccurs="1" name="HappyTailDetailsResult" type="tns:ArrayOfHappyTailDetailItem" />
          </s:sequence>
        </s:complexType>
      </s:element>
      <s:element name="boolean" type="s:boolean" />
      <s:element name="ArrayOfXmlNode" nillable="true" type="tns:ArrayOfXmlNode" />
      <s:element name="ArrayOfAnyType" nillable="true" type="tns:ArrayOfAnyType" />
      <s:element name="ArrayOfHappyTailDetailItem" nillable="true" type="tns:ArrayOfHappyTailDetailItem" />
    </s:schema>
  </wsdl:types>
  <wsdl:message name="MedicalViewReportPdfSoapIn">
    <wsdl:part name="parameters" element="tns:MedicalViewReportPdf" />
  </wsdl:message>
  <wsdl:message name="MedicalViewReportPdfSoapOut">
    <wsdl:part name="parameters" element="tns:MedicalViewReportPdfResponse" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsSoapIn">
    <wsdl:part name="parameters" element="tns:AdoptionDetails" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsSoapOut">
    <wsdl:part name="parameters" element="tns:AdoptionDetailsResponse" />
  </wsdl:message>
  <wsdl:message name="AdoptionListSoapIn">
    <wsdl:part name="parameters" element="tns:AdoptionList" />
  </wsdl:message>
  <wsdl:message name="AdoptionListSoapOut">
    <wsdl:part name="parameters" element="tns:AdoptionListResponse" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchSoapIn">
    <wsdl:part name="parameters" element="tns:AdoptableSearch" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchSoapOut">
    <wsdl:part name="parameters" element="tns:AdoptableSearchResponse" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageSoapIn">
    <wsdl:part name="parameters" element="tns:AdoptableSearchWithStage" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageSoapOut">
    <wsdl:part name="parameters" element="tns:AdoptableSearchWithStageResponse" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsSoapIn">
    <wsdl:part name="parameters" element="tns:AdoptableDetails" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsSoapOut">
    <wsdl:part name="parameters" element="tns:AdoptableDetailsResponse" />
  </wsdl:message>
  <wsdl:message name="foundSearchSoapIn">
    <wsdl:part name="parameters" element="tns:foundSearch" />
  </wsdl:message>
  <wsdl:message name="foundSearchSoapOut">
    <wsdl:part name="parameters" element="tns:foundSearchResponse" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupSoapIn">
    <wsdl:part name="parameters" element="tns:foundSearchForCompanyGroup" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupSoapOut">
    <wsdl:part name="parameters" element="tns:foundSearchForCompanyGroupResponse" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableSoapIn">
    <wsdl:part name="parameters" element="tns:foundSearchForCompanyGroupPageable" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableSoapOut">
    <wsdl:part name="parameters" element="tns:foundSearchForCompanyGroupPageableResponse" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteSoapIn">
    <wsdl:part name="parameters" element="tns:foundSearchWithSite" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteSoapOut">
    <wsdl:part name="parameters" element="tns:foundSearchWithSiteResponse" />
  </wsdl:message>
  <wsdl:message name="lostSearchSoapIn">
    <wsdl:part name="parameters" element="tns:lostSearch" />
  </wsdl:message>
  <wsdl:message name="lostSearchSoapOut">
    <wsdl:part name="parameters" element="tns:lostSearchResponse" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupSoapIn">
    <wsdl:part name="parameters" element="tns:lostSearchForCompanyGroup" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupSoapOut">
    <wsdl:part name="parameters" element="tns:lostSearchForCompanyGroupResponse" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableSoapIn">
    <wsdl:part name="parameters" element="tns:lostSearchForCompanyGroupPageable" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableSoapOut">
    <wsdl:part name="parameters" element="tns:lostSearchForCompanyGroupPageableResponse" />
  </wsdl:message>
  <wsdl:message name="foundDetailsSoapIn">
    <wsdl:part name="parameters" element="tns:foundDetails" />
  </wsdl:message>
  <wsdl:message name="foundDetailsSoapOut">
    <wsdl:part name="parameters" element="tns:foundDetailsResponse" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupSoapIn">
    <wsdl:part name="parameters" element="tns:foundDetailsForCompanyGroup" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupSoapOut">
    <wsdl:part name="parameters" element="tns:foundDetailsForCompanyGroupResponse" />
  </wsdl:message>
  <wsdl:message name="lostDetailsSoapIn">
    <wsdl:part name="parameters" element="tns:lostDetails" />
  </wsdl:message>
  <wsdl:message name="lostDetailsSoapOut">
    <wsdl:part name="parameters" element="tns:lostDetailsResponse" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupSoapIn">
    <wsdl:part name="parameters" element="tns:lostDetailsForCompanyGroup" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupSoapOut">
    <wsdl:part name="parameters" element="tns:lostDetailsForCompanyGroupResponse" />
  </wsdl:message>
  <wsdl:message name="HappyTailListSoapIn">
    <wsdl:part name="parameters" element="tns:HappyTailList" />
  </wsdl:message>
  <wsdl:message name="HappyTailListSoapOut">
    <wsdl:part name="parameters" element="tns:HappyTailListResponse" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsSoapIn">
    <wsdl:part name="parameters" element="tns:HappyTailDetails" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsSoapOut">
    <wsdl:part name="parameters" element="tns:HappyTailDetailsResponse" />
  </wsdl:message>
  <wsdl:message name="MedicalViewReportPdfHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authKey" type="s:string" />
    <wsdl:part name="ftpDestination" type="s:string" />
  </wsdl:message>
  <wsdl:message name="MedicalViewReportPdfHttpGetOut">
    <wsdl:part name="Body" element="tns:boolean" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authKey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="AdoptionListHttpGetIn">
    <wsdl:part name="authKey" type="s:string" />
    <wsdl:part name="adoptionDate" type="s:string" />
    <wsdl:part name="siteID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptionListHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchHttpGetIn">
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="location" type="s:string" />
    <wsdl:part name="site" type="s:string" />
    <wsdl:part name="onHold" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="primaryBreed" type="s:string" />
    <wsdl:part name="secondaryBreed" type="s:string" />
    <wsdl:part name="specialNeeds" type="s:string" />
    <wsdl:part name="noDogs" type="s:string" />
    <wsdl:part name="noCats" type="s:string" />
    <wsdl:part name="noKids" type="s:string" />
    <wsdl:part name="stageID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageHttpGetIn">
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="location" type="s:string" />
    <wsdl:part name="site" type="s:string" />
    <wsdl:part name="onHold" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="primaryBreed" type="s:string" />
    <wsdl:part name="secondaryBreed" type="s:string" />
    <wsdl:part name="specialNeeds" type="s:string" />
    <wsdl:part name="noDogs" type="s:string" />
    <wsdl:part name="noCats" type="s:string" />
    <wsdl:part name="noKids" type="s:string" />
    <wsdl:part name="stageID" type="s:string" />
    <wsdl:part name="featured" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="foundSearchHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
    <wsdl:part name="skip" type="s:string" />
    <wsdl:part name="take" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
    <wsdl:part name="siteID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableHttpGetIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="skip" type="s:string" />
    <wsdl:part name="take" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundDetailsHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundDetailsHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="lostDetailsHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostDetailsHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupHttpGetIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupHttpGetOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="HappyTailListHttpGetIn">
    <wsdl:part name="pAuthKey" type="s:string" />
    <wsdl:part name="pSpeciesID" type="s:string" />
    <wsdl:part name="pSiteID" type="s:string" />
    <wsdl:part name="pOrderBy" type="s:string" />
    <wsdl:part name="pCount" type="s:string" />
    <wsdl:part name="pFeaturedPet" type="s:string" />
  </wsdl:message>
  <wsdl:message name="HappyTailListHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfAnyType" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsHttpGetIn">
    <wsdl:part name="pAuthkey" type="s:string" />
    <wsdl:part name="pAdoptionID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsHttpGetOut">
    <wsdl:part name="Body" element="tns:ArrayOfHappyTailDetailItem" />
  </wsdl:message>
  <wsdl:message name="MedicalViewReportPdfHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authKey" type="s:string" />
    <wsdl:part name="ftpDestination" type="s:string" />
  </wsdl:message>
  <wsdl:message name="MedicalViewReportPdfHttpPostOut">
    <wsdl:part name="Body" element="tns:boolean" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authKey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptionDetailsHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="AdoptionListHttpPostIn">
    <wsdl:part name="authKey" type="s:string" />
    <wsdl:part name="adoptionDate" type="s:string" />
    <wsdl:part name="siteID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptionListHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchHttpPostIn">
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="location" type="s:string" />
    <wsdl:part name="site" type="s:string" />
    <wsdl:part name="onHold" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="primaryBreed" type="s:string" />
    <wsdl:part name="secondaryBreed" type="s:string" />
    <wsdl:part name="specialNeeds" type="s:string" />
    <wsdl:part name="noDogs" type="s:string" />
    <wsdl:part name="noCats" type="s:string" />
    <wsdl:part name="noKids" type="s:string" />
    <wsdl:part name="stageID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageHttpPostIn">
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="location" type="s:string" />
    <wsdl:part name="site" type="s:string" />
    <wsdl:part name="onHold" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="primaryBreed" type="s:string" />
    <wsdl:part name="secondaryBreed" type="s:string" />
    <wsdl:part name="specialNeeds" type="s:string" />
    <wsdl:part name="noDogs" type="s:string" />
    <wsdl:part name="noCats" type="s:string" />
    <wsdl:part name="noKids" type="s:string" />
    <wsdl:part name="stageID" type="s:string" />
    <wsdl:part name="featured" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableSearchWithStageHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="AdoptableDetailsHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="foundSearchHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
    <wsdl:part name="skip" type="s:string" />
    <wsdl:part name="take" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchForCompanyGroupPageableHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="searchOption" type="s:string" />
    <wsdl:part name="siteID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundSearchWithSiteHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableHttpPostIn">
    <wsdl:part name="speciesID" type="s:string" />
    <wsdl:part name="sex" type="s:string" />
    <wsdl:part name="ageGroup" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
    <wsdl:part name="orderBy" type="s:string" />
    <wsdl:part name="skip" type="s:string" />
    <wsdl:part name="take" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostSearchForCompanyGroupPageableHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfXmlNode" />
  </wsdl:message>
  <wsdl:message name="foundDetailsHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundDetailsHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="foundDetailsForCompanyGroupHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="lostDetailsHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostDetailsHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupHttpPostIn">
    <wsdl:part name="animalID" type="s:string" />
    <wsdl:part name="authkey" type="s:string" />
  </wsdl:message>
  <wsdl:message name="lostDetailsForCompanyGroupHttpPostOut">
    <wsdl:part name="Body" />
  </wsdl:message>
  <wsdl:message name="HappyTailListHttpPostIn">
    <wsdl:part name="pAuthKey" type="s:string" />
    <wsdl:part name="pSpeciesID" type="s:string" />
    <wsdl:part name="pSiteID" type="s:string" />
    <wsdl:part name="pOrderBy" type="s:string" />
    <wsdl:part name="pCount" type="s:string" />
    <wsdl:part name="pFeaturedPet" type="s:string" />
  </wsdl:message>
  <wsdl:message name="HappyTailListHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfAnyType" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsHttpPostIn">
    <wsdl:part name="pAuthkey" type="s:string" />
    <wsdl:part name="pAdoptionID" type="s:string" />
  </wsdl:message>
  <wsdl:message name="HappyTailDetailsHttpPostOut">
    <wsdl:part name="Body" element="tns:ArrayOfHappyTailDetailItem" />
  </wsdl:message>
  <wsdl:portType name="WsAdoptionSoap">
    <wsdl:operation name="MedicalViewReportPdf">
      <wsdl:input message="tns:MedicalViewReportPdfSoapIn" />
      <wsdl:output message="tns:MedicalViewReportPdfSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <wsdl:input message="tns:AdoptionDetailsSoapIn" />
      <wsdl:output message="tns:AdoptionDetailsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <wsdl:input message="tns:AdoptionListSoapIn" />
      <wsdl:output message="tns:AdoptionListSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <wsdl:input message="tns:AdoptableSearchSoapIn" />
      <wsdl:output message="tns:AdoptableSearchSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <wsdl:input message="tns:AdoptableSearchWithStageSoapIn" />
      <wsdl:output message="tns:AdoptableSearchWithStageSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <wsdl:input message="tns:AdoptableDetailsSoapIn" />
      <wsdl:output message="tns:AdoptableDetailsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <wsdl:input message="tns:foundSearchSoapIn" />
      <wsdl:output message="tns:foundSearchSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <wsdl:input message="tns:foundSearchForCompanyGroupSoapIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <wsdl:input message="tns:foundSearchForCompanyGroupPageableSoapIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupPageableSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <wsdl:input message="tns:foundSearchWithSiteSoapIn" />
      <wsdl:output message="tns:foundSearchWithSiteSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <wsdl:input message="tns:lostSearchSoapIn" />
      <wsdl:output message="tns:lostSearchSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <wsdl:input message="tns:lostSearchForCompanyGroupSoapIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <wsdl:input message="tns:lostSearchForCompanyGroupPageableSoapIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupPageableSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <wsdl:input message="tns:foundDetailsSoapIn" />
      <wsdl:output message="tns:foundDetailsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <wsdl:input message="tns:foundDetailsForCompanyGroupSoapIn" />
      <wsdl:output message="tns:foundDetailsForCompanyGroupSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <wsdl:input message="tns:lostDetailsSoapIn" />
      <wsdl:output message="tns:lostDetailsSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <wsdl:input message="tns:lostDetailsForCompanyGroupSoapIn" />
      <wsdl:output message="tns:lostDetailsForCompanyGroupSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <wsdl:input message="tns:HappyTailListSoapIn" />
      <wsdl:output message="tns:HappyTailListSoapOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <wsdl:input message="tns:HappyTailDetailsSoapIn" />
      <wsdl:output message="tns:HappyTailDetailsSoapOut" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:portType name="WsAdoptionHttpGet">
    <wsdl:operation name="MedicalViewReportPdf">
      <wsdl:input message="tns:MedicalViewReportPdfHttpGetIn" />
      <wsdl:output message="tns:MedicalViewReportPdfHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <wsdl:input message="tns:AdoptionDetailsHttpGetIn" />
      <wsdl:output message="tns:AdoptionDetailsHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <wsdl:input message="tns:AdoptionListHttpGetIn" />
      <wsdl:output message="tns:AdoptionListHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <wsdl:input message="tns:AdoptableSearchHttpGetIn" />
      <wsdl:output message="tns:AdoptableSearchHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <wsdl:input message="tns:AdoptableSearchWithStageHttpGetIn" />
      <wsdl:output message="tns:AdoptableSearchWithStageHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <wsdl:input message="tns:AdoptableDetailsHttpGetIn" />
      <wsdl:output message="tns:AdoptableDetailsHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <wsdl:input message="tns:foundSearchHttpGetIn" />
      <wsdl:output message="tns:foundSearchHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <wsdl:input message="tns:foundSearchForCompanyGroupHttpGetIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <wsdl:input message="tns:foundSearchForCompanyGroupPageableHttpGetIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupPageableHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <wsdl:input message="tns:foundSearchWithSiteHttpGetIn" />
      <wsdl:output message="tns:foundSearchWithSiteHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <wsdl:input message="tns:lostSearchHttpGetIn" />
      <wsdl:output message="tns:lostSearchHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <wsdl:input message="tns:lostSearchForCompanyGroupHttpGetIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <wsdl:input message="tns:lostSearchForCompanyGroupPageableHttpGetIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupPageableHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <wsdl:input message="tns:foundDetailsHttpGetIn" />
      <wsdl:output message="tns:foundDetailsHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <wsdl:input message="tns:foundDetailsForCompanyGroupHttpGetIn" />
      <wsdl:output message="tns:foundDetailsForCompanyGroupHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <wsdl:input message="tns:lostDetailsHttpGetIn" />
      <wsdl:output message="tns:lostDetailsHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <wsdl:input message="tns:lostDetailsForCompanyGroupHttpGetIn" />
      <wsdl:output message="tns:lostDetailsForCompanyGroupHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <wsdl:input message="tns:HappyTailListHttpGetIn" />
      <wsdl:output message="tns:HappyTailListHttpGetOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <wsdl:input message="tns:HappyTailDetailsHttpGetIn" />
      <wsdl:output message="tns:HappyTailDetailsHttpGetOut" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:portType name="WsAdoptionHttpPost">
    <wsdl:operation name="MedicalViewReportPdf">
      <wsdl:input message="tns:MedicalViewReportPdfHttpPostIn" />
      <wsdl:output message="tns:MedicalViewReportPdfHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <wsdl:input message="tns:AdoptionDetailsHttpPostIn" />
      <wsdl:output message="tns:AdoptionDetailsHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <wsdl:input message="tns:AdoptionListHttpPostIn" />
      <wsdl:output message="tns:AdoptionListHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <wsdl:input message="tns:AdoptableSearchHttpPostIn" />
      <wsdl:output message="tns:AdoptableSearchHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <wsdl:input message="tns:AdoptableSearchWithStageHttpPostIn" />
      <wsdl:output message="tns:AdoptableSearchWithStageHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <wsdl:input message="tns:AdoptableDetailsHttpPostIn" />
      <wsdl:output message="tns:AdoptableDetailsHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <wsdl:input message="tns:foundSearchHttpPostIn" />
      <wsdl:output message="tns:foundSearchHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <wsdl:input message="tns:foundSearchForCompanyGroupHttpPostIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <wsdl:input message="tns:foundSearchForCompanyGroupPageableHttpPostIn" />
      <wsdl:output message="tns:foundSearchForCompanyGroupPageableHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <wsdl:input message="tns:foundSearchWithSiteHttpPostIn" />
      <wsdl:output message="tns:foundSearchWithSiteHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <wsdl:input message="tns:lostSearchHttpPostIn" />
      <wsdl:output message="tns:lostSearchHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <wsdl:input message="tns:lostSearchForCompanyGroupHttpPostIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <wsdl:input message="tns:lostSearchForCompanyGroupPageableHttpPostIn" />
      <wsdl:output message="tns:lostSearchForCompanyGroupPageableHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <wsdl:input message="tns:foundDetailsHttpPostIn" />
      <wsdl:output message="tns:foundDetailsHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <wsdl:input message="tns:foundDetailsForCompanyGroupHttpPostIn" />
      <wsdl:output message="tns:foundDetailsForCompanyGroupHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <wsdl:input message="tns:lostDetailsHttpPostIn" />
      <wsdl:output message="tns:lostDetailsHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <wsdl:input message="tns:lostDetailsForCompanyGroupHttpPostIn" />
      <wsdl:output message="tns:lostDetailsForCompanyGroupHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <wsdl:input message="tns:HappyTailListHttpPostIn" />
      <wsdl:output message="tns:HappyTailListHttpPostOut" />
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <wsdl:input message="tns:HappyTailDetailsHttpPostIn" />
      <wsdl:output message="tns:HappyTailDetailsHttpPostOut" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="WsAdoptionSoap" type="tns:WsAdoptionSoap">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="MedicalViewReportPdf">
      <soap:operation soapAction="http://www.petango.com/MedicalViewReportPdf" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <soap:operation soapAction="http://www.petango.com/AdoptionDetails" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <soap:operation soapAction="http://www.petango.com/AdoptionList" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <soap:operation soapAction="http://www.petango.com/AdoptableSearch" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <soap:operation soapAction="http://www.petango.com/AdoptableSearchWithStage" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <soap:operation soapAction="http://www.petango.com/AdoptableDetails" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <soap:operation soapAction="http://www.petango.com/foundSearch" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <soap:operation soapAction="http://www.petango.com/foundSearchForCompanyGroup" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <soap:operation soapAction="http://www.petango.com/foundSearchForCompanyGroupPageable" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <soap:operation soapAction="http://www.petango.com/foundSearchWithSite" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <soap:operation soapAction="http://www.petango.com/lostSearch" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <soap:operation soapAction="http://www.petango.com/lostSearchForCompanyGroup" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <soap:operation soapAction="http://www.petango.com/lostSearchForCompanyGroupPageable" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <soap:operation soapAction="http://www.petango.com/foundDetails" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <soap:operation soapAction="http://www.petango.com/foundDetailsForCompanyGroup" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <soap:operation soapAction="http://www.petango.com/lostDetails" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <soap:operation soapAction="http://www.petango.com/lostDetailsForCompanyGroup" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <soap:operation soapAction="http://www.petango.com/HappyTailList" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <soap:operation soapAction="http://www.petango.com/HappyTailDetails" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:binding name="WsAdoptionSoap12" type="tns:WsAdoptionSoap">
    <soap12:binding transport="http://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="MedicalViewReportPdf">
      <soap12:operation soapAction="http://www.petango.com/MedicalViewReportPdf" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <soap12:operation soapAction="http://www.petango.com/AdoptionDetails" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <soap12:operation soapAction="http://www.petango.com/AdoptionList" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <soap12:operation soapAction="http://www.petango.com/AdoptableSearch" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <soap12:operation soapAction="http://www.petango.com/AdoptableSearchWithStage" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <soap12:operation soapAction="http://www.petango.com/AdoptableDetails" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <soap12:operation soapAction="http://www.petango.com/foundSearch" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <soap12:operation soapAction="http://www.petango.com/foundSearchForCompanyGroup" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <soap12:operation soapAction="http://www.petango.com/foundSearchForCompanyGroupPageable" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <soap12:operation soapAction="http://www.petango.com/foundSearchWithSite" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <soap12:operation soapAction="http://www.petango.com/lostSearch" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <soap12:operation soapAction="http://www.petango.com/lostSearchForCompanyGroup" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <soap12:operation soapAction="http://www.petango.com/lostSearchForCompanyGroupPageable" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <soap12:operation soapAction="http://www.petango.com/foundDetails" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <soap12:operation soapAction="http://www.petango.com/foundDetailsForCompanyGroup" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <soap12:operation soapAction="http://www.petango.com/lostDetails" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <soap12:operation soapAction="http://www.petango.com/lostDetailsForCompanyGroup" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <soap12:operation soapAction="http://www.petango.com/HappyTailList" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <soap12:operation soapAction="http://www.petango.com/HappyTailDetails" style="document" />
      <wsdl:input>
        <soap12:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap12:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:binding name="WsAdoptionHttpGet" type="tns:WsAdoptionHttpGet">
    <http:binding verb="GET" />
    <wsdl:operation name="MedicalViewReportPdf">
      <http:operation location="/MedicalViewReportPdf" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <http:operation location="/AdoptionDetails" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <http:operation location="/AdoptionList" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <http:operation location="/AdoptableSearch" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <http:operation location="/AdoptableSearchWithStage" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <http:operation location="/AdoptableDetails" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <http:operation location="/foundSearch" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <http:operation location="/foundSearchForCompanyGroup" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <http:operation location="/foundSearchForCompanyGroupPageable" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <http:operation location="/foundSearchWithSite" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <http:operation location="/lostSearch" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <http:operation location="/lostSearchForCompanyGroup" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <http:operation location="/lostSearchForCompanyGroupPageable" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <http:operation location="/foundDetails" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <http:operation location="/foundDetailsForCompanyGroup" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <http:operation location="/lostDetails" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <http:operation location="/lostDetailsForCompanyGroup" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <http:operation location="/HappyTailList" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <http:operation location="/HappyTailDetails" />
      <wsdl:input>
        <http:urlEncoded />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:binding name="WsAdoptionHttpPost" type="tns:WsAdoptionHttpPost">
    <http:binding verb="POST" />
    <wsdl:operation name="MedicalViewReportPdf">
      <http:operation location="/MedicalViewReportPdf" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionDetails">
      <http:operation location="/AdoptionDetails" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptionList">
      <http:operation location="/AdoptionList" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearch">
      <http:operation location="/AdoptableSearch" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableSearchWithStage">
      <http:operation location="/AdoptableSearchWithStage" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AdoptableDetails">
      <http:operation location="/AdoptableDetails" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearch">
      <http:operation location="/foundSearch" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroup">
      <http:operation location="/foundSearchForCompanyGroup" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchForCompanyGroupPageable">
      <http:operation location="/foundSearchForCompanyGroupPageable" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundSearchWithSite">
      <http:operation location="/foundSearchWithSite" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearch">
      <http:operation location="/lostSearch" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroup">
      <http:operation location="/lostSearchForCompanyGroup" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostSearchForCompanyGroupPageable">
      <http:operation location="/lostSearchForCompanyGroupPageable" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetails">
      <http:operation location="/foundDetails" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="foundDetailsForCompanyGroup">
      <http:operation location="/foundDetailsForCompanyGroup" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetails">
      <http:operation location="/lostDetails" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="lostDetailsForCompanyGroup">
      <http:operation location="/lostDetailsForCompanyGroup" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:content part="Body" type="text/xml" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailList">
      <http:operation location="/HappyTailList" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="HappyTailDetails">
      <http:operation location="/HappyTailDetails" />
      <wsdl:input>
        <mime:content type="application/x-www-form-urlencoded" />
      </wsdl:input>
      <wsdl:output>
        <mime:mimeXml part="Body" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="WsAdoption">
    <wsdl:port name="WsAdoptionSoap" binding="tns:WsAdoptionSoap">
      <soap:address location="https://ws.petango.com/webservices/wsadoption.asmx" />
    </wsdl:port>
    <wsdl:port name="WsAdoptionSoap12" binding="tns:WsAdoptionSoap12">
      <soap12:address location="https://ws.petango.com/webservices/wsadoption.asmx" />
    </wsdl:port>
    <wsdl:port name="WsAdoptionHttpGet" binding="tns:WsAdoptionHttpGet">
      <http:address location="https://ws.petango.com/webservices/wsadoption.asmx" />
    </wsdl:port>
    <wsdl:port name="WsAdoptionHttpPost" binding="tns:WsAdoptionHttpPost">
      <http:address location="https://ws.petango.com/webservices/wsadoption.asmx" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
../
