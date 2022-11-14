<?xml version="1.0" encoding="utf-8"?>
<Element>
    <PropertyPalette>
        <Tab TextId="1001" Text="Allgemein">
            <Expander TextId="1004" Text="Geometrie">
                <Node ID="yxqxaevwqusutctcautvvexctewcfcvd" />
                <Node ID="wxfwbduftysctywxaapaebtvswpfvrpw" />
            </Expander>
            <Expander TextId="1008" Text="Norm" />
            <Expander TextId="1011" Text="Betondeckung">
                <Node ID="dqptqqffbbdctpptbxesbeestcdrydce" />
                <Node ID="ttxfsetyucvttudaxtvwxddbbrxpeaex" />
                <Node ID="fwpdcfrytpuytfrqbvcvfyayypwptuxx" />
            </Expander>
            <Expander TextId="1017" Text="Material">
                <Node ID="wxtpfrtxuyvftrtayvfbpbqbaresstcy" />
                <Node ID="efvptwywvwcxtfcfxebqbwxxwfwuxpec" />
            </Expander>
        </Tab>
        <Tab TextId="1019" Text="Ring Bewehrun">
            <Expander TextId="1022" Text="Neue Gruppe">
                <Node ID="csrwpvbursfxtvpayvuffaqbabawtcyv" />
                <Node ID="dwscqxrfyppbteyeavxbqbxywcwyvpsw" />
                <Node ID="byrbwtdrtpastcafbccbertsywcwtfcc" />
                <Node ID="vtcbrveptcqctwyfywyyautdtcdqvfwu" />
            </Expander>
            <Expander TextId="1030" Text="Ganghöhenbereiche">
                <Node ID="axftdexyewsqtrpeyxwtwwvtbvecdffb" />
                <Node ID="sbxxybtaawputcapycrcxswdppepawvb" />
                <Node ID="udxepyrxravytqdqxwqwvfvrfdeuryec" />
                <Node ID="ubabpwcwduactxfcavypdxdsfxfefrux" />
            </Expander>
        </Tab>
        <Tab TextId="1035" Text="Längsstäbe">
            <Expander TextId="1036" Text="Neue Gruppe">
                <Node ID="qbtduusabsyattsrbcbacuvbxxcwteqc" />
                <Node ID="fvxvxxtyxwautudcxfwpcupssepacpbc" />
                <Node ID="aefprsdutqdatcyqxxvtewaseecrdyur" />
            </Expander>
            <Expander TextId="1002" Text="Bend in the upper part">
                <Node ID="xsspcaxssrcutycrycuqcsevypyceqru" />
                <Node ID="vvxevdcubtaxtuuuysrrxrbeaacpuewb" />
                <Node ID="cwafsqewyttqtvvuaxteyqberbptycuv" />
            </Expander>
        </Tab>
        <Tab TextId="1020" Text="Format">
            <Expander TextId="1021" Text="Neue Gruppe">
                <Node ID="dtxqxtsbswustdtqxpqayeeesdfesqbp" />
            </Expander>
        </Tab>
        <Tab IsDefault="true" Text="Unassigned">
            <Expander Text="Format cylinder">
                <Node ID="wxerbruyxacstdxwbspsuedyvwpuyqqc" />
            </Expander>
        </Tab>
    </PropertyPalette>
    <Script>
        <Name>NodeScript.py</Name>
        <Title>NodeScript</Title>
        <Version>1.4.1</Version>
        <Interactor>True</Interactor>
        <ReadLastInput>True</ReadLastInput>
        <SubElements>AugerPileReinfocement.pyp</SubElements>
        <VSPlacementPointInput>False</VSPlacementPointInput>
        <VSMultiPlacement>False</VSMultiPlacement>
    </Script>
    <SubElement>
        <PyP>Etc\VisualScripts\Palettes\General\NodeTopPlaneReferencePalette.pypsub</PyP>
        <Uuid>477A70FF-6471-439F-852F-FD0C7337BC72</Uuid>
        <Name>TopPlaneReferencePalette</Name>
        <ID>wxfwbduftysctywxaapaebtvswpfvrpw</ID>
        <Position X="1424.1827002496348" Y="-506.48642892745352" />
        <DefaultValues>
            <DefaultValue Name="SelectedPlaneReferences" TextId="1033" Text="Oberkante">PlaneReferences(Bottomdependency(1)Topdependency(2)Bottomelevation(0.000000)Topelevation(0.000000)Maxheight(0.000000)UpperReferencePlaneID(ModelGuid(00000000-0000-0000-0000-000000000000)PlaneID(-1))LowerReferencePlaneID(ModelGuid(00000000-0000-0000-0000-000000000000)PlaneID(-1))AbsBottomElevation(0.000000)AbsTopElevation(2500.000000))</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeLengthInput.pypsub</PyP>
        <Uuid>tcrspdvfuabxtdupacswqfxrrqaesrcu</Uuid>
        <Name>Height</Name>
        <ID>wcaweqqxsruxtdtdbqqqefxrarswrspv</ID>
        <Position X="1296.7847222222219" Y="110.22222222222194" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="Length" TextId="1007" Text="Höhe">10000.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeOperatorSubtraction.pypsub</PyP>
        <Uuid>xpwvxvxsuefrtwfsxwddbdutvfytxdcf</Uuid>
        <Name>OperatorSubtraction</Name>
        <ID>qctwwfaqrdqatacbxwstrwfbwrvpaswb</ID>
        <Position X="1643.1827002496348" Y="-88.569762260786888" />
        <Constraints>
            <Constraint Name="Value">
                <Link NodeId="wxfwbduftysctywxaapaebtvswpfvrpw" Name="TopElevation" />
            </Constraint>
            <Constraint Name="SubtractionValue">
                <Link NodeId="wcaweqqxsruxtdtdbqqqefxrarswrspv" Name="Length" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Objects\NodeCylinder.pypsub</PyP>
        <Uuid>rvacdvrwddwctqtpbvtuwaevxasbusyq</Uuid>
        <Name>Cylinder</Name>
        <ID>yxqxaevwqusutctcautvvexctewcfcvd</ID>
        <Position X="1899.2261904761915" Y="-46.142857142857622" />
        <DefaultValues>
            <DefaultValue Name="CenterPoint" Visible="false">Point3D(0.0, 0.0, -7500.0)</DefaultValue>
            <DefaultValue Name="CenterPoint.X" Visible="false" />
            <DefaultValue Name="CenterPoint.Y" Visible="false" />
            <DefaultValue Name="CenterPoint.Z" Visible="false" />
            <DefaultValue Name="DirectionVector" Visible="false" />
            <DefaultValue Name="DirectionVector.X" Visible="false" />
            <DefaultValue Name="DirectionVector.Y" Visible="false" />
            <DefaultValue Name="DirectionVector.Z" Visible="false" />
            <DefaultValue Name="Radius">500.0</DefaultValue>
            <DefaultValue Name="Height">10000.0</DefaultValue>
            <DefaultValue Name="CenterPointZPosition" Visible="false" />
            <DefaultValue Name="TopOpen" Visible="false" />
            <DefaultValue Name="BottomOpen" Visible="false" />
            <DefaultValue Name="CreateModelPreviewObjects">True</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="CenterPoint.Z">
                <Link NodeId="qctwwfaqrdqatacbxwstrwfbwrvpaswb" Name="Result" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\General\NodeFormat.pypsub</PyP>
        <Uuid>fwreertcpssftedeadfwdwffedpfteau</Uuid>
        <Name>Format cylinder</Name>
        <ID>wxerbruyxacstdxwbspsuedyvwpuyqqc</ID>
        <Position X="2406.86904761905" Y="449.38095238095275" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="Layer">3735</DefaultValue>
            <DefaultValue Name="Pen">1</DefaultValue>
            <DefaultValue Name="Stroke">1</DefaultValue>
            <DefaultValue Name="Color">1</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="Objects">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Cylinder" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeOperatorAddition.pypsub</PyP>
        <Uuid>tqbypwdbcbsutvayarxurxvyduyaxfcw</Uuid>
        <Name>X cylinder right</Name>
        <ID>eewyxxqcpcpbtpabyfdpeqcwewwepcwy</ID>
        <Position X="2923.0041288210655" Y="138.45404726302394" />
        <Constraints>
            <Constraint Name="Value1">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="CenterPoint.X" />
            </Constraint>
            <Constraint Name="Value2">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Radius" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeConcreteGradeComboBox.pypsub</PyP>
        <Uuid>7d176944-eaae-4e34-96e2-c4522507a14e</Uuid>
        <Name>ConcreteGrade</Name>
        <ID>wxtpfrtxuyvftrtayvfbpbqbaresstcy</ID>
        <Position X="665.66666666666686" Y="684.49999999999966" />
        <DefaultValues>
            <DefaultValue Name="ConcreteGrade">4</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeSteelGradeComboBox.pypsub</PyP>
        <Uuid>85d6ec0a-0202-4e18-ad12-ba10f672cf53</Uuid>
        <Name>SteelGrade</Name>
        <ID>efvptwywvwcxtfcfxebqbwxxwfwuxpec</ID>
        <Position X="837.75000000000011" Y="800.00000000000011" />
        <DefaultValues>
            <DefaultValue Name="SteelGrade">4</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeConcreteCoverComboBox.pypsub</PyP>
        <Uuid>312d11d2-a6f8-44b8-94e9-f58ad136a130</Uuid>
        <Name>Cover start</Name>
        <ID>fwpdcfrytpuytfrqbvcvfyayypwptuxx</ID>
        <Position X="1044.25" Y="926.83333333333258" />
        <DefaultValues>
            <DefaultValue Name="ConcreteCover" TextId="1013" Text="Unten">25.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeConcreteCoverComboBox.pypsub</PyP>
        <Uuid>312d11d2-a6f8-44b8-94e9-f58ad136a130</Uuid>
        <Name>Cover contour</Name>
        <ID>ttxfsetyucvttudaxtvwxddbbrxpeaex</ID>
        <Position X="1221.7500000000002" Y="1037.4166666666665" />
        <DefaultValues>
            <DefaultValue Name="ConcreteCover" TextId="1015" Text="Wendel">25.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeConcreteCoverComboBox.pypsub</PyP>
        <Uuid>312d11d2-a6f8-44b8-94e9-f58ad136a130</Uuid>
        <Name>Cover end</Name>
        <ID>dqptqqffbbdctpptbxesbeestcdrydce</ID>
        <Position X="1407.3055555555554" Y="1125.1944444444448" />
        <DefaultValues>
            <DefaultValue Name="ConcreteCover" TextId="1012" Text="Oben">25.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeBarDiameterComboBox.pypsub</PyP>
        <Uuid>28227ca1-65ac-4c8e-9b38-16b8186e2a14</Uuid>
        <Name>BarDiameterComboBox</Name>
        <ID>csrwpvbursfxtvpayvuffaqbabawtcyv</ID>
        <Position X="655.0833333333336" Y="1335.2499999999998" />
        <DefaultValues>
            <DefaultValue Name="BarDiameter">12.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeLengthInput.pypsub</PyP>
        <Uuid>tcrspdvfuabxtdupacswqfxrrqaesrcu</Uuid>
        <Name>Pitch</Name>
        <ID>dwscqxrfyppbteyeavxbqbxywcwyvpsw</ID>
        <Position X="863.39872619186792" Y="1434.333333333333" />
        <DefaultValues>
            <DefaultValue Name="Length" TextId="1023" Text="Ganghöhe">250.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeIntegerInput.pypsub</PyP>
        <Uuid>uqsfceccrxwytsrearuaftcvxsdauape</Uuid>
        <Name>Loops start</Name>
        <ID>vtcbrveptcqctwyfywyyautdtcdqvfwu</ID>
        <Position X="654.06539285853444" Y="1598.3962423228631" />
        <DefaultValues>
            <DefaultValue Name="Value" TextId="1025" Text="Ringe am Fuß">1</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeIntegerInput.pypsub</PyP>
        <Uuid>uqsfceccrxwytsrearuaftcvxsdauape</Uuid>
        <Name>Loops end</Name>
        <ID>byrbwtdrtpastcafbccbertsywcwtfcc</ID>
        <Position X="901.73205952520118" Y="1669.8962423228631" />
        <DefaultValues>
            <DefaultValue Name="Value" TextId="1024" Text="Ringe am Kopf">1</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeMultiLengthInput.pypsub</PyP>
        <Uuid>13d2a411-1aa1-4eaa-8b93-fae06d6906af</Uuid>
        <Name>Bottom outside</Name>
        <ID>ubabpwcwduactxfcavypdxdsfxfefrux</ID>
        <Position X="1468.8031214950677" Y="1977.9737775327576" />
        <DefaultValues>
            <DefaultValue Name="ShowValuesInOneRow">True</DefaultValue>
            <DefaultValue Name="LengthsRowText">Fuß aussen</DefaultValue>
            <DefaultValue Name="Length1" TextId="1041" Text="Länge">2000.0</DefaultValue>
            <DefaultValue Name="Length2" TextId="1043" Text="Ganghöhe">100.0</DefaultValue>
            <DefaultValue Name="Length3" Visible="false" />
            <DefaultValue Name="Length4" Visible="false" />
            <DefaultValue Name="Length5" Visible="false" />
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeMultiLengthInput.pypsub</PyP>
        <Uuid>13d2a411-1aa1-4eaa-8b93-fae06d6906af</Uuid>
        <Name>Bottom inside</Name>
        <ID>udxepyrxravytqdqxwqwvfvrfdeuryec</ID>
        <Position X="1483.8621041790502" Y="2366.9540264505058" />
        <DefaultValues>
            <DefaultValue Name="ShowValuesInOneRow">True</DefaultValue>
            <DefaultValue Name="LengthsRowText">Fuß innen</DefaultValue>
            <DefaultValue Name="Length1" TextId="1047" Text="Länge" />
            <DefaultValue Name="Length2" TextId="1044" Text="Ganghöhe" />
            <DefaultValue Name="Length3" Visible="false" />
            <DefaultValue Name="Length4" Visible="false" />
            <DefaultValue Name="Length5" Visible="false" />
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeMultiLengthInput.pypsub</PyP>
        <Uuid>13d2a411-1aa1-4eaa-8b93-fae06d6906af</Uuid>
        <Name>Top inside</Name>
        <ID>sbxxybtaawputcapycrcxswdppepawvb</ID>
        <Position X="1745.3369418413877" Y="2560.7746433336238" />
        <DefaultValues>
            <DefaultValue Name="ShowValuesInOneRow">True</DefaultValue>
            <DefaultValue Name="LengthsRowText">Kopf innen</DefaultValue>
            <DefaultValue Name="Length1" TextId="1048" Text="Länge" />
            <DefaultValue Name="Length2" TextId="1045" Text="Ganghöhe" />
            <DefaultValue Name="Length3" Visible="false" />
            <DefaultValue Name="Length4" Visible="false" />
            <DefaultValue Name="Length5" Visible="false" />
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeMultiLengthInput.pypsub</PyP>
        <Uuid>13d2a411-1aa1-4eaa-8b93-fae06d6906af</Uuid>
        <Name>Top outside</Name>
        <ID>axftdexyewsqtrpeyxwtwwvtbvecdffb</ID>
        <Position X="2047.2744418413877" Y="2697.2973706063508" />
        <DefaultValues>
            <DefaultValue Name="ShowValuesInOneRow">True</DefaultValue>
            <DefaultValue Name="ShowLengthsHeader">True</DefaultValue>
            <DefaultValue Name="LengthsRowText">Kopf aussen</DefaultValue>
            <DefaultValue Name="Length1" TextId="1049" Text="Länge">2000.0</DefaultValue>
            <DefaultValue Name="Length2" TextId="1046" Text="Ganghöhe">100.0</DefaultValue>
            <DefaultValue Name="Length3" Visible="false" />
            <DefaultValue Name="Length4" Visible="false" />
            <DefaultValue Name="Length5" Visible="false" />
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Palettes\Layout\NodeFormatPalette.pypsub</PyP>
        <Uuid>df10f303-a36b-441c-af39-205c01972da4</Uuid>
        <Name>FormatPalette</Name>
        <ID>dtxqxtsbswustdtqxpqayeeesdfesqbp</ID>
        <Position X="673.30853275047866" Y="1823.8333333333328" />
        <DefaultValues>
            <DefaultValue Name="Layer">3735</DefaultValue>
            <DefaultValue Name="Pen">1</DefaultValue>
            <DefaultValue Name="Stroke">1</DefaultValue>
            <DefaultValue Name="Color">5</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Reinforcement\Objects\NodeSpiralReinforcement.pypsub</PyP>
        <Uuid>e0b59443-da02-487d-b715-efef2c2da96a</Uuid>
        <Name>SpiralReinforcement</Name>
        <ID>btfpydpdexcdttrfxuxsuudqsbxbvyey</ID>
        <Position X="2435.5" Y="892.83333333333337" />
        <DefaultValues>
            <DefaultValue Name="CreateModelObjects">True</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="PlacementPoint">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="CenterPoint" />
            </Constraint>
            <Constraint Name="Radius">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Radius" />
            </Constraint>
            <Constraint Name="Height">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Height" />
            </Constraint>
            <Constraint Name="ConcreteGrade">
                <Link NodeId="wxtpfrtxuyvftrtayvfbpbqbaresstcy" Name="ConcreteGrade" />
            </Constraint>
            <Constraint Name="SteelGrade">
                <Link NodeId="efvptwywvwcxtfcfxebqbwxxwfwuxpec" Name="SteelGrade" />
            </Constraint>
            <Constraint Name="ConcreteCoverStart">
                <Link NodeId="fwpdcfrytpuytfrqbvcvfyayypwptuxx" Name="ConcreteCover" />
            </Constraint>
            <Constraint Name="ConcreteCoverContour">
                <Link NodeId="ttxfsetyucvttudaxtvwxddbbrxpeaex" Name="ConcreteCover" />
            </Constraint>
            <Constraint Name="ConcreteCoverEnd">
                <Link NodeId="dqptqqffbbdctpptbxesbeestcdrydce" Name="ConcreteCover" />
            </Constraint>
            <Constraint Name="Diameter">
                <Link NodeId="csrwpvbursfxtvpayvuffaqbabawtcyv" Name="BarDiameter" />
            </Constraint>
            <Constraint Name="Pitch">
                <Link NodeId="dwscqxrfyppbteyeavxbqbxywcwyvpsw" Name="Length" />
            </Constraint>
            <Constraint Name="LoopsStart">
                <Link NodeId="vtcbrveptcqctwyfywyyautdtcdqvfwu" Name="Value" />
            </Constraint>
            <Constraint Name="LoopsEnd">
                <Link NodeId="byrbwtdrtpastcafbccbertsywcwtfcc" Name="Value" />
            </Constraint>
            <Constraint Name="Length1">
                <Link NodeId="ubabpwcwduactxfcavypdxdsfxfefrux" Name="Length1" />
            </Constraint>
            <Constraint Name="Pitch1">
                <Link NodeId="ubabpwcwduactxfcavypdxdsfxfefrux" Name="Length2" />
            </Constraint>
            <Constraint Name="Length2">
                <Link NodeId="udxepyrxravytqdqxwqwvfvrfdeuryec" Name="Length1" />
            </Constraint>
            <Constraint Name="Pitch2">
                <Link NodeId="udxepyrxravytqdqxwqwvfvrfdeuryec" Name="Length2" />
            </Constraint>
            <Constraint Name="Length3">
                <Link NodeId="sbxxybtaawputcapycrcxswdppepawvb" Name="Length1" />
            </Constraint>
            <Constraint Name="Pitch3">
                <Link NodeId="sbxxybtaawputcapycrcxswdppepawvb" Name="Length2" />
            </Constraint>
            <Constraint Name="Length4">
                <Link NodeId="axftdexyewsqtrpeyxwtwwvtbvecdffb" Name="Length1" />
            </Constraint>
            <Constraint Name="Pitch4">
                <Link NodeId="axftdexyewsqtrpeyxwtwwvtbvecdffb" Name="Length2" />
            </Constraint>
            <Constraint Name="FormatProperties">
                <Link NodeId="dtxqxtsbswustdtqxpqayeeesdfesqbp" Name="FormatProperties" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\ReinforcementResourceControls\NodeBarDiameterComboBox.pypsub</PyP>
        <Uuid>28227ca1-65ac-4c8e-9b38-16b8186e2a14</Uuid>
        <Name>Longi diameter</Name>
        <ID>fvxvxxtyxwautudcxfwpcupssepacpbc</ID>
        <Position X="2799.5457954877324" Y="-139.27809559411878" />
        <DefaultValues>
            <DefaultValue Name="BarDiameter" TextId="1038" Text="Durchmesser">25.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeOperatorHalve.pypsub</PyP>
        <Uuid>6fdcbb04-a679-4e14-8a26-80793ff9f1dd</Uuid>
        <Name>Longi diam / 2</Name>
        <ID>pwbwaarpevwatxtbyyusrqsrwcqwurbq</ID>
        <Position X="3012.7184145353508" Y="-126.75103931706263" />
        <Constraints>
            <Constraint Name="Value">
                <Link NodeId="fvxvxxtyxwautudcxfwpcupssepacpbc" Name="BarDiameter" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeMassSubtraction.pypsub</PyP>
        <Uuid>stfpvdrquyestwdsyxturvbwqwbvbayp</Uuid>
        <Name>Longitudinal x</Name>
        <ID>utsbwpffpadftdwcasdwuyabxftttbqv</ID>
        <Position X="3227.8612716782068" Y="174.21992027889559" />
        <Constraints>
            <Constraint Name="Value">
                <Link NodeId="eewyxxqcpcpbtpabyfdpeqcwewwepcwy" Name="Result" />
            </Constraint>
            <Constraint Name="SubtractionValues">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="ConcreteCoverContour" />
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="Diameter" />
                <Link NodeId="pwbwaarpevwatxtbyyusrqsrwcqwurbq" Name="Result" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeOperatorAddition.pypsub</PyP>
        <Uuid>tqbypwdbcbsutvayarxurxvyduyaxfcw</Uuid>
        <Name>Longitudinal y start</Name>
        <ID>cwrufypvuwqdtutvafveqvdebwwsdetx</ID>
        <Position X="3237.8612716782068" Y="376.858809167786" />
        <Visible>False</Visible>
        <Constraints>
            <Constraint Name="Value1">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="CenterPoint.Z" />
            </Constraint>
            <Constraint Name="Value2">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="ConcreteCoverStart" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeLengthInput.pypsub</PyP>
        <Uuid>tcrspdvfuabxtdupacswqfxrrqaesrcu</Uuid>
        <Name>Top overhang</Name>
        <ID>aefprsdutqdatcyqxxvtewaseecrdyur</ID>
        <Position X="2789.7023809523839" Y="1162.2375942028273" />
        <DefaultValues>
            <DefaultValue Name="Length" TextId="1042" Text="Überstand oben">1000.0</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeOperatorNegative.pypsub</PyP>
        <Uuid>udruqyedbbaetpfsapcccdwqauvptwbs</Uuid>
        <Name>OperatorNegative</Name>
        <ID>bppptpceadsttqwcaxuaudufuedaufre</ID>
        <Position X="3008.1037930411635" Y="930.71378467901707" />
        <Constraints>
            <Constraint Name="Value">
                <Link NodeId="aefprsdutqdatcyqxxvtewaseecrdyur" Name="Length" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Workflow\NodeOutputTrueFalseSwitcher.pypsub</PyP>
        <Uuid>75392DFE-C50A-40AA-B149-696B4431DEC7</Uuid>
        <Name>Top cover ?</Name>
        <ID>ywudctuvqecbterybafqytppcuqyetds</ID>
        <Position X="3225.6478045851763" Y="1012.2303791956119" />
        <Constraints>
            <Constraint Name="ConditionValue">
                <Link NodeId="bppptpceadsttqwcaxuaudufuedaufre" Name="Value" />
            </Constraint>
            <Constraint Name="Object">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="ConcreteCoverEnd" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\Operators\NodeMassSubtraction.pypsub</PyP>
        <Uuid>stfpvdrquyestwdsyxturvbwqwbvbayp</Uuid>
        <Name>Height - cover|overhang</Name>
        <ID>dpwapevvaseatryexfsrrxusurexbtcw</ID>
        <Position X="3388.4179233553036" Y="669.49200645724409" />
        <Constraints>
            <Constraint Name="Value">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Height" />
            </Constraint>
            <Constraint Name="SubtractionValues">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="ConcreteCoverStart" />
                <Link NodeId="ywudctuvqecbterybafqytppcuqyetds" Name="FalseOutputObject" />
                <Link NodeId="bppptpceadsttqwcaxuaudufuedaufre" Name="Result" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Curves\NodeLine3DByPointVector.pypsub</PyP>
        <Uuid>63fccdf8-8718-49ef-88c2-91cb6ff5a05a</Uuid>
        <Name>Bar axis</Name>
        <ID>cwfxwtstytbbtcvebpevdtqrafwvusvr</ID>
        <Position X="3587.0297559671362" Y="-75.102510137274152" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="StartPoint">Point3D(450.5, 0.0, -7475.0)</DefaultValue>
            <DefaultValue Name="StartPoint.X" Visible="false" />
            <DefaultValue Name="StartPoint.Y" Visible="false" />
            <DefaultValue Name="StartPoint.Z" Visible="false" />
            <DefaultValue Name="EndVector">Vector3D(0.0, 0.0, 10975.0)</DefaultValue>
            <DefaultValue Name="EndVector.Z" Visible="false" />
            <DefaultValue Name="CreateHandles">False</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="StartPoint.X">
                <Link NodeId="utsbwpffpadftdwcasdwuyabxftttbqv" Name="Result" />
            </Constraint>
            <Constraint Name="StartPoint.Y">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="CenterPoint.Y" />
            </Constraint>
            <Constraint Name="StartPoint.Z">
                <Link NodeId="cwrufypvuwqdtutvafveqvdebwwsdetx" Name="Result" />
            </Constraint>
            <Constraint Name="EndVector.Z">
                <Link NodeId="dpwapevvaseatryexfsrrxusurexbtcw" Name="Result" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\NodeCheckboxInput.pypsub</PyP>
        <Uuid>wqpsqybfdwwdtrvrxfswyqfuuvwqrqvw</Uuid>
        <Name>CheckboxInput</Name>
        <ID>xsspcaxssrcutycrycuqcsevypyceqru</ID>
        <Position X="3472.5018595720612" Y="430.58826653837355" />
        <DefaultValues>
            <DefaultValue Name="Checkbox" TextId="1003" Text="Add bend" />
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeLengthInput.pypsub</PyP>
        <Uuid>tcrspdvfuabxtdupacswqfxrrqaesrcu</Uuid>
        <Name>LengthInput</Name>
        <ID>vvxevdcubtaxtuuuysrrxrbeaacpuewb</ID>
        <Position X="3682.3956342756187" Y="654.12458076762232" />
        <DefaultValues>
            <DefaultValue Name="Length">500.0</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="IsVisible">
                <Link NodeId="xsspcaxssrcutycrycuqcsevypyceqru" Name="Checkbox" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeAngleInput.pypsub</PyP>
        <Uuid>584663E4-2421-4BB1-944A-08DAEF8DB98A</Uuid>
        <Name>AngleInput</Name>
        <ID>cwafsqewyttqtvvuaxteyqberbptycuv</ID>
        <Position X="3682.3956342756187" Y="850.99958076762232" />
        <Constraints>
            <Constraint Name="IsVisible">
                <Link NodeId="xsspcaxssrcutycrycuqcsevypyceqru" Name="Checkbox" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Vector\NodeVector3DByLength.pypsub</PyP>
        <Uuid>epddcxrvywbvtxubyvepsqesyydawqwc</Uuid>
        <Name>Vector3DByLength</Name>
        <ID>aceetwpuryrytrqyyftcvquepvpqxrvd</ID>
        <Position X="3949.5831342756187" Y="708.24958076762232" />
        <Visible>False</Visible>
        <Constraints>
            <Constraint Name="Length">
                <Link NodeId="vvxevdcubtaxtuuuysrrxrbeaacpuewb" Name="Length" />
            </Constraint>
            <Constraint Name="YAngle">
                <Link NodeId="cwafsqewyttqtvvuaxteyqberbptycuv" Name="Angle" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Curves\NodeLine3DByPointVector.pypsub</PyP>
        <Uuid>63fccdf8-8718-49ef-88c2-91cb6ff5a05a</Uuid>
        <Name>Line3DByPointVector</Name>
        <ID>usuppyxwsvtptyrpxbfqvqdaesqqywvf</ID>
        <Position X="3777.7081342756187" Y="390.06208076762243" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="CreateHandles">False</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="StartPoint">
                <Link NodeId="cwfxwtstytbbtcvebpevdtqrafwvusvr" Name="Line.EndPoint" />
            </Constraint>
            <Constraint Name="EndVector">
                <Link NodeId="aceetwpuryrytrqyyftcvquepvpqxrvd" Name="Vector" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\InputControls\Edit\NodeIntegerInput.pypsub</PyP>
        <Uuid>uqsfceccrxwytsrearuaftcvxsdauape</Uuid>
        <Name>Longitudinal count</Name>
        <ID>qbtduusabsyattsrbcbacuvbxxcwteqc</ID>
        <Position X="3961.8720941890297" Y="-447.88794407896864" />
        <DefaultValues>
            <DefaultValue Name="Value" TextId="1034" Text="Anzahl">20</DefaultValue>
        </DefaultValues>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Curves\NodeLine3DByPointVector.pypsub</PyP>
        <Uuid>63fccdf8-8718-49ef-88c2-91cb6ff5a05a</Uuid>
        <Name>Line3DByPointVector</Name>
        <ID>wxbcdutdrtyvtcfpaewuvbpdcwfqtbpr</ID>
        <Position X="2370.4756434130213" Y="-348.16167319643785" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="EndVector">Vector3D(0.0, 0.0, 10000.0)</DefaultValue>
            <DefaultValue Name="EndVector.Z" Visible="false" />
            <DefaultValue Name="CreateHandles">False</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="StartPoint">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="CenterPoint" />
            </Constraint>
            <Constraint Name="EndVector.Z">
                <Link NodeId="yxqxaevwqusutctcautvvexctewcfcvd" Name="Height" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\General\NodeConvertDataType.pypsub</PyP>
        <Uuid>B543081A-75F8-4497-8571-075BD0792208</Uuid>
        <Name>ConvertDataType</Name>
        <ID>uqtptxvuyqdqtupfbcuaqerwyspeeedu</ID>
        <Position X="3825.9418299277918" Y="147.56578630121936" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="TargetType" Visible="false">1246</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="Source">
                <Link NodeId="vvxevdcubtaxtuuuysrrxrbeaacpuewb" Name="Length" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Math\LogicalOperators\NodeOperatorAnd.pypsub</PyP>
        <Uuid>180CDB6E-43AD-4924-8F58-903721C4FB6D</Uuid>
        <Name>OperatorAnd</Name>
        <ID>aurtspuqwrvfteweaeadvxfdpayfwvfp</ID>
        <Position X="4015.6836777538806" Y="-82.7331267422588" />
        <Constraints>
            <Constraint Name="Value1">
                <Link NodeId="xsspcaxssrcutycrycuqcsevypyceqru" Name="Checkbox" />
            </Constraint>
            <Constraint Name="Value2">
                <Link NodeId="uqtptxvuyqdqtupfbcuaqerwyspeeedu" Name="Output" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Geometry\Curves\NodePolyline3D.pypsub</PyP>
        <Uuid>qavyfbpysxvrtfsxycrwpwwveuyffrxf</Uuid>
        <Name>Polyline3D</Name>
        <ID>fbpfyqyvuysftyswarrqtwcpvcyarafc</ID>
        <Position X="4044.8956342756192" Y="239.06776258580427" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="PointCount">3</DefaultValue>
            <DefaultValue Name="CreateHandles">False</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="Points">
                <Link NodeId="cwfxwtstytbbtcvebpevdtqrafwvusvr" Name="Line.StartPoint" />
                <Link NodeId="cwfxwtstytbbtcvebpevdtqrafwvusvr" Name="Line.EndPoint" />
                <Link NodeId="usuppyxwsvtptyrpxbfqvqdaesqqywvf" Name="Line.EndPoint" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Workflow\Select\NodeOutputTrueFalseSelector.pypsub</PyP>
        <Uuid>4F00A78D-9F71-4496-9406-127E3F223517</Uuid>
        <Name>OutputTrueFalseSelector</Name>
        <ID>ryqyweeuqefytvttatssywbwpcuvdqcx</ID>
        <Position X="4344.8400512716662" Y="-62.52561686083601" />
        <Constraints>
            <Constraint Name="ConditionValue">
                <Link NodeId="aurtspuqwrvfteweaeadvxfdpayfwvfp" Name="Result" />
            </Constraint>
            <Constraint Name="TrueConditionObject">
                <Link NodeId="fbpfyqyvuysftyswarrqtwcpvcyarafc" Name="Polyline" />
            </Constraint>
            <Constraint Name="FalseConditionObject">
                <Link NodeId="cwfxwtstytbbtcvebpevdtqrafwvusvr" Name="Line" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Reinforcement\BarShape\NodeBarsByPolyline.pypsub</PyP>
        <Uuid>uyapcxtssveqtwbpxsuqdrfbpbdrcxev</Uuid>
        <Name>Logitudinal bar</Name>
        <ID>dwxsrtsqevadtbswaxyyudaayrvuytpv</ID>
        <Position X="4721.9178192972577" Y="-95.755909446933" />
        <Visible>False</Visible>
        <DefaultValues>
            <DefaultValue Name="ReinforcementShapeBarProperties">ReinforcementShapeBarProperties(ConcreteGrade(4), SteelGrade(4), Diameter(25.0), BendingRoller(4.0))</DefaultValue>
            <DefaultValue Name="ReinforcementShapeBarProperties.ConcreteGrade" Visible="false" />
            <DefaultValue Name="ReinforcementShapeBarProperties.SteelGrade" Visible="false" />
            <DefaultValue Name="ReinforcementShapeBarProperties.BarDiameter" Visible="false" />
            <DefaultValue Name="ReinforcementShapeBarProperties.BendingRoller" Visible="false" />
        </DefaultValues>
        <Constraints>
            <Constraint Name="Polyline">
                <Link NodeId="ryqyweeuqefytvttatssywbwpcuvdqcx" Name="OutputObject" />
            </Constraint>
            <Constraint Name="ReinforcementShapeBarProperties.ConcreteGrade">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="ConcreteGrade" />
            </Constraint>
            <Constraint Name="ReinforcementShapeBarProperties.SteelGrade">
                <Link NodeId="btfpydpdexcdttrfxuxsuudqsbxbvyey" Name="SteelGrade" />
            </Constraint>
            <Constraint Name="ReinforcementShapeBarProperties.BarDiameter">
                <Link NodeId="pwbwaarpevwatxtbyyusrqsrwcqwurbq" Name="Value" />
            </Constraint>
        </Constraints>
    </SubElement>
    <SubElement>
        <PyP>Etc\VisualScripts\Reinforcement\Objects\NodeBarRotationalPlacement.pypsub</PyP>
        <Uuid>7b9dc706-ffa1-49b4-bbb0-59db156d0722</Uuid>
        <Name>BarRotationalPlacement</Name>
        <ID>rprptfepadpxtspebqerafsxtqpfvtav</ID>
        <Position X="4357.1827002496348" Y="-406.79892892745357" />
        <DefaultValues>
            <DefaultValue Name="CreateModelObjects">True</DefaultValue>
        </DefaultValues>
        <Constraints>
            <Constraint Name="BarCount">
                <Link NodeId="qbtduusabsyattsrbcbacuvbxxcwteqc" Name="Value" />
            </Constraint>
            <Constraint Name="RotationAxis">
                <Link NodeId="wxbcdutdrtyvtcfpaewuvbpdcwfqtbpr" Name="Line" />
            </Constraint>
            <Constraint Name="BendingShape">
                <Link NodeId="dwxsrtsqevadtbswaxyyudaayrvuytpv" Name="Bars" />
            </Constraint>
        </Constraints>
    </SubElement>
</Element>