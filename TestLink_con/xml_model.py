# -*- coding: utf-8 -*-


class Tlink:
    def __init__(self):
        self.model = """
                        <testcase internalid="{t_id}" name="{name_input}">
                            <node_order><![CDATA[100]]></node_order>
                            <externalid><![CDATA[]]></externalid>
                            <version><![CDATA[1]]></version>
                            <summary><![CDATA[]]></summary>
                            <preconditions><![CDATA[]]></preconditions>
                            <execution_type><![CDATA[1]]></execution_type>
                            <importance><![CDATA[{importance_input}]]></importance>
                        <steps>
                        <step>
                            <step_number><![CDATA[1]]></step_number>
                            <actions><![CDATA[<p>{actions_input}</p>]]></actions>
                            <expectedresults><![CDATA[<p>{expectedresults_input}</p>]]></expectedresults>
                            <execution_type><![CDATA[1]]></execution_type>
                        </step>
                        </steps>
                        </testcase>
                        """

    # def t_link_xml(self):
    #     self.model = """<?xml version="1.0" encoding="UTF-8"?>
    #                     <testcases>
    #                     <testcase internalid="{internalid_input}" name="{name_input}">
    #                         <node_order><![CDATA[100]]></node_order>
    #                         <externalid><![CDATA[5438]]></externalid>
    #                         <version><![CDATA[1]]></version>
    #                         <summary><![CDATA[]]></summary>
    #                         <preconditions><![CDATA[]]></preconditions>
    #                         <execution_type><![CDATA[1]]></execution_type>
    #                         <importance><![CDATA[{importance_input}]]></importance>
    #                     <steps>
    #                     <step>
    #                         <step_number><![CDATA[1]]></step_number>
    #                         <actions><![CDATA[<p>{actions_input}</p>]]></actions>
    #                         <expectedresults><![CDATA[<p>{expectedresults_input}</p>]]></expectedresults>
    #                         <execution_type><![CDATA[1]]></execution_type>
    #                     </step>
    #                     </steps>
    #                     </testcase>
    #                     </testcases>"""
    #     return self.model.format(self, internalid_input='9527', name_input='', importance_input='3',
    #                              actions_input='test action',
    #                              expectedresults_input='test')
    #     return self.model
    def initial(self):
        xml_head = b'''<?xml version="1.0" encoding="UTF-8"?>
                        <testcases>'''
        with open('test.xml', 'wb') as head:
            head.write(xml_head)

    def fin(self):
        xml_end = b'''</testcases>'''
        with open('test.xml', 'ab') as head:
            head.write(xml_end)

    def to_file(self, file):
        with open('test.xml', 'ab') as temp:
            temp.write(file)
        print('write done')


