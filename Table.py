from Driver import Driver


class Table(Driver):
    
    @staticmethod
    def get_elem_by_index(index, table):
        return table.find_element_by_xpath(f'.//li[{index}]')
